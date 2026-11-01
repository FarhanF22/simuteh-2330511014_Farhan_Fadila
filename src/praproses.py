"""praproses.py: rangkaian praproses SIMUTEH (dipakai ulang mulai P5).

Urutan: ubah ukuran -> koreksi gamma -> CLAHE kanal V -> redam derau -> tajamkan.
Semua parameter ada di PARAM_BAWAAN dan disimpan ke JSON agar dapat ditelusuri.
Fungsi yang sama dipakai untuk data latih dan data uji (lihat P5.4).
"""
import json
import cv2
import numpy as np

PARAM_BAWAAN = {
    "lebar": 640,            
    "gamma": 1.0,           
    "clahe_clip": 0.0,       
    "clahe_tile": 8,
    "penapis": "median",     
    "kernel": 3,
    "sigma": 1.0,
    "tajam_k": 0.0,          
}


def _ganjil(k):
    """Kernel penapis harus ganjil dan minimal 1."""
    k = int(k)
    return max(1, k if k % 2 == 1 else k + 1)


def praproses(img_bgr, p=None):
    """Urutan: ubah ukuran -> gamma -> CLAHE kanal V -> redam derau -> tajamkan."""
    p = {**PARAM_BAWAAN, **(p or {})}

    h, w = img_bgr.shape[:2]
    if w != p["lebar"]:
        tinggi = int(round(h * p["lebar"] / w))
        img = cv2.resize(img_bgr, (int(p["lebar"]), tinggi),
                         interpolation=cv2.INTER_AREA)
    else:
        img = img_bgr.copy()

    if p["gamma"] != 1:
        lut = np.array([255 * (i / 255) ** p["gamma"] for i in range(256)])
        img = cv2.LUT(img, lut.clip(0, 255).astype(np.uint8))

    if p["clahe_clip"] > 0:
        clahe = cv2.createCLAHE(clipLimit=float(p["clahe_clip"]),
                                tileGridSize=(int(p["clahe_tile"]),) * 2)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv[:, :, 2] = clahe.apply(hsv[:, :, 2])
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    k = _ganjil(p["kernel"])
    if p["penapis"] == "rerata":
        img = cv2.blur(img, (k, k))
    elif p["penapis"] == "gaussian":
        img = cv2.GaussianBlur(img, (k, k), float(p["sigma"]))
    elif p["penapis"] == "median":
        img = cv2.medianBlur(img, k)
    elif p["penapis"] != "none":
        raise ValueError(f"penapis tidak dikenal: {p['penapis']}")

    if p["tajam_k"] > 0:
        blur = cv2.GaussianBlur(img, (5, 5), float(p["sigma"]))
        img = cv2.addWeighted(img, 1 + p["tajam_k"], blur, -p["tajam_k"], 0)
    return img


def simpan_param(p, path="../hasil/param_praproses.json"):
    with open(path, "w") as f:
        json.dump({**PARAM_BAWAAN, **p}, f, indent=2)


def muat_param(path="../hasil/param_praproses.json"):
    with open(path) as f:
        return {**PARAM_BAWAAN, **json.load(f)}


def param_adaptif(img_bgr, dasar=None, ambang_bayangan=40):
    """Opsional (P5.2): pilih CLAHE otomatis dari statistik citra.

    CLAHE hanya diaktifkan bila kecerahan tepi kiri dan kanan berbeda jauh
    (ciri bayangan sebagian). Pada kondisi lain CLAHE justru menaikkan
    keragaman daun sehat sehingga dimatikan.
    """
    p = {**PARAM_BAWAAN, **(dasar or {})}
    g = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    seperempat = g.shape[1] // 4
    beda = abs(float(g[:, :seperempat].mean()) - float(g[:, -seperempat:].mean()))
    p["clahe_clip"] = 2.0 if beda > ambang_bayangan else 0.0
    return p
