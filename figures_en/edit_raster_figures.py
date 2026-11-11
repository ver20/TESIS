"""Translate the text of Figures 5 and 10, which only exist as raster images.

Figure 5 (ROC curves): the Spanish legend entries and axis labels are painted
over and rewritten in English with the same font (DejaVu Sans, matplotlib's
default) and size, so the curves themselves are untouched.
Figure 10 (application screenshots): the panel titles are translated. The
screenshots themselves show the Spanish user interface of the app.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
DJV = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LIB = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def fig5():
    im = Image.open(os.path.join(HERE, "src_fig05_es.png")).convert("RGB")
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(DJV, 37)
    # legend rows (y-span of the original text) -> new label
    rows = {(1385, 1418): "Neural network (AUC = 0.814)",
            (1494, 1531): "Logistic regression (AUC = 0.789)",
            (1549, 1589): "Decision tree (AUC = 0.770)"}
    for (y0, y1), txt in rows.items():
        d.rectangle([1498, y0 - 4, 2140, y1 + 3], fill="white")
        d.text((1501, (y0 + y1) / 2 + 2), txt, font=f, fill="black", anchor="lm")
    f = ImageFont.truetype(DJV, 41)   # axis labels are larger than the legend
    # x label
    d.rectangle([700, 1705, 1680, 1765], fill="white")
    d.text(((739 + 1628) / 2, 1713), "False positive rate (1 − specificity)", font=f,
           fill="black", anchor="mt")
    # y label (rotated)
    d.rectangle([40, 700, 86, 980], fill="white")
    lab = Image.new("RGB", (400, 50), "white")
    ImageDraw.Draw(lab).text((200, 25), "Sensitivity", font=f, fill="black", anchor="mm")
    lab = lab.rotate(90, expand=True)
    im.paste(lab, (63 - 25, int((718 + 960) / 2) - 200))
    im.save(os.path.join(HERE, "fig05_roc_curves.png"))


def fig10():
    im = Image.open(os.path.join(HERE, "src_fig10_es.png")).convert("RGB")
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(LIB, 34)
    s = 2300 / 2000
    titles = [((5, 3), "(a) Individual assessment"),
              ((1013, 3), "(b) Score explanation"),
              ((5, 525), "(c) Group assessment"),
              ((1013, 525), "(d) Territorial risk map")]
    for (x, y), t in titles:
        X, Y = int(x * s), int(y * s)
        d.rectangle([X, Y, X + int(560 * s), Y + int(44 * s)], fill="white")
        d.text((X + 4, Y + int(22 * s)), t, font=f, fill="#111", anchor="lm")
    im.save(os.path.join(HERE, "fig10_application_screens.png"))


if __name__ == "__main__":
    fig5()
    fig10()
    print("done")
