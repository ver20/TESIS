"""Swap the Spanish figures inside the article PDF for the English ones.
Usage: python replace_in_pdf.py input.pdf output.pdf"""
import os, sys, zlib
import pikepdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
# PDF object number of each figure image (from `pdfimages -list`)
MAP = {10: "fig01_crisp_dm_workflow", 11: "fig02_endes_integration", 25: "fig03_architecture",
       31: "fig04_prevalence_trend", 36: "fig05_roc_curves", 37: "fig06_confusion_matrix",
       44: "fig07_shap_global_importance", 45: "fig08_shap_local_explanation",
       51: "fig09_factor_weight_by_department", 52: "fig10_application_screens"}

pdf = pikepdf.open(sys.argv[1])
for num, name in MAP.items():
    obj = pdf.get_object((num, 0))
    im = Image.open(os.path.join(HERE, name + ".png"))
    if im.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", im.size, "white"); bg.paste(im.convert("RGBA"), mask=im.convert("RGBA").split()[3]); im = bg
    im = im.convert("RGB")
    assert (im.width, im.height) == (int(obj.Width), int(obj.Height)), name
    obj.write(zlib.compress(im.tobytes(), 9), filter=pikepdf.Name.FlateDecode)
    obj.ColorSpace = pikepdf.Name.DeviceRGB
    obj.BitsPerComponent = 8
    for k in ("/SMask", "/DecodeParms"):
        if k in obj:
            del obj[k]
pdf.save(sys.argv[2])
print("saved", sys.argv[2])
