"""English version of the ethics approval (DICTAMEN_DE_ETICA.docx -> ETHICS_APPROVAL_EN.docx).
Text is replaced run by run so the original formatting (bold labels, fonts, table) is kept."""
import sys
import docx

SCHOOL = "School of Systems Engineering"
COMMITTEE = f"Ethics Committee of the {SCHOOL}"
UNI = "Universidad Peruana Unión"


def put(par, texts):
    """Assign texts to the paragraph's runs in order; extra runs are emptied."""
    runs = par.runs
    assert len(texts) <= len(runs), (par.text[:40], len(runs))
    for r, t in zip(runs, texts + [""] * (len(runs) - len(texts))):
        r.text = t


P = {
    0: ["UNIVERSIDAD PERUANA UNIÓN"],
    1: ["Faculty of Engineering and Architecture"],
    2: [COMMITTEE],
    4: ["ETHICS APPROVAL"],
    5: ["No.", " _______-2026-CE-", "FIA", "-UPeU"],
    6: ["Lima, ", "November", " ", "11", ",", "", " 2026"],
    7: ["I. Details of the study"],
    8: ["II. Background"],
    9: ["The research team submitted to this Committee a request for the ethical review of the study, enclosing the "
        "research protocol, the relevance assessment instrument to be administered to the panel of health "
        "professionals, the informed consent form for the panel members and the supporting documentation required "
        "by this Committee."],
    10: ["The manuscript to be submitted to the journal Nutrition (Elsevier) must report the name of the responsible "
         "ethics committee, the approval number and how the informed consent of the participants was handled, in "
         "accordance with publication ethics standards."],
    12: ["III. Committee review"],
    13: [f"The {COMMITTEE} of {UNI} has reviewed the study in accordance with the principles of the Declaration of "
         "Helsinki of the World Medical Association, the CIOMS International Ethical Guidelines for Health-related "
         "Research Involving Humans, Law No. 29733, the Personal Data Protection Law, and its regulations, the "
         f"National Code of Scientific Integrity of CONCYTEC and the Code of Ethics for Research of {UNI}."],
    14: ["The Committee finds that:"],
    15: ["a)  ", "The study uses only publicly available secondary microdata from the ENDES 2007–2025, collected by INEI "
         "for statistical purposes with the informed consent of the respondents. It involves no intervention, contact, "
         "interview or procedure of any kind with the children or with their mothers or caregivers."],
    16: ["b)  ", "The microdata are published without names, addresses, identity document numbers or any other direct "
         "identifier. The HHID and CASEID keys, assigned by INEI, were used only to merge the modules and to link each "
         "child to their mother. The analyzed dataset is anonymous and does not allow the re-identification of the "
         "children or their families."],
    17: ["c)  ", "The study does not expose participants to physical, psychological or social risk. The only theoretical "
         "risk is to confidentiality, which is mitigated by prohibiting any re-identification procedure or linkage with "
         "external sources and by publishing only results aggregated at the national, departmental and natural-region "
         "levels."],
    18: ["d)  ", "New consent from the survey participants is not required, since it was obtained by INEI during the "
         "ENDES fieldwork and the data are publicly released for research. Furthermore, contacting again the families "
         "of 304,271 children surveyed between 2007 and 2025 throughout the country is materially impracticable."],
    19: ["e)  ", "Once the study is approved, the relevance of the application will be assessed by a panel of four health "
         "professionals, with voluntary participation and prior informed consent, using an instrument based on TAM2. "
         "The instrument does not collect sensitive data and the responses will be analyzed in aggregate form, "
         "without individual identification."],
    20: ["f)  ", "Results will be published only in aggregate form; no person can be identified and no decision about "
         "any individual participant derives from the study. The application is a support tool that does not replace "
         "clinical judgment and will not be used with patients."],
    21: ["g)  ", "The study contributes knowledge on the factors associated with childhood stunting and their territorial "
         "distribution, a priority problem on the national health agenda, for the benefit of the population from which "
         "the data originate. The code and the derived dataset will be published in Zenodo without identifiers."],
    22: ["IV. Decision"],
    23: [f"On the basis of the foregoing review, the {COMMITTEE} of {UNI}:"],
    25: ["FIRST. APPROVES ", "from an ethical standpoint the protocol of the study entitled ",
         "\"Predictive model of the risk of childhood stunting in Peru using machine learning\" (original title: "
         "\"Modelo Predictivo de Riesgo de Desnutrición Crónica Infantil en el Perú mediante Machine Learning\")",
         ", as it complies with the ethical principles and regulations applicable to research with personal data and "
         "with human participants."],
    26: ["SECOND. AUTHORIZES ", "the waiver of new informed consent", " ",
         "for the analysis of the ENDES microdata, having verified that these are public and anonymized secondary "
         "data whose consent was obtained by INEI; that their use involves no risk beyond the minimal risk to "
         "confidentiality, which is adequately mitigated; that contacting participants again is materially "
         "impracticable; and that the waiver does not affect the rights or interests of the participants. It also "
         "APPROVES the assessment instrument and the informed consent form for the panel of health professionals, "
         "whose participation must be voluntary and documented with that consent before the instrument is "
         "administered."],
    27: ["THIRD. ", "ESTABLISHES that this approval is limited to the design described in the reviewed protocol. Any "
         "substantial modification must be reported to the Committee for its consideration."],
    28: ["FOURTH. ", "REQUIRES the investigators to send the Committee a copy of the resulting publication and to report "
         "any event or finding that compromises the confidentiality of the information."],
    29: ["This decision is issued in accordance with the Declaration of Helsinki of the World Medical Association, the "
         "CIOMS International Ethical Guidelines, Law No. 29733 on Personal Data Protection, the National Code of "
         f"Scientific Integrity of CONCYTEC and the Code of Ethics for Research of {UNI}."],
    30: ["This decision is issued at the request of the applicant, for the corresponding editorial purposes."],
}

T = {  # (row, col): texts
    (0, 0): ["Title"],
    (0, 1): ["Predictive model of the risk of childhood stunting in Peru using machine learning (original title: "
             "Modelo Predictivo de Riesgo de Desnutrición Crónica Infantil en el Perú mediante Machine Learning)"],
    (1, 0): ["Principal investigator"],
    (1, 1): ["MSc. ", "Nemias", " Saboya Ríos (ORCID 0000-0002-7166-2197)"],
    (2, 0): ["Co-investigators"],
    (3, 0): ["Academic unit"],
    (3, 1): [f"{SCHOOL}, Faculty of Engineering and Architecture"],
    (4, 0): ["Research line"],
    (4, 1): ["Data science"],
    (5, 0): ["Study type"],
    (5, 1): ["Observational, retrospective, analytical — development and internal validation of a predictive model "
             "on public secondary data, with a relevance assessment by an expert panel"],
    (6, 0): ["Data source"],
    (6, 1): ["Public microdata from the Demographic and Family Health Survey (ENDES) 2007–2025, collected and published "
             "by the National Institute of Statistics and Informatics (INEI): modules RECH0, RECH1, RECH6, RECH23, "
             "REC41 and REC21"],
    (7, 0): ["Population"],
    (7, 1): ["304,271 children under five years of age with valid anthropometry; panel of four health professionals "
             "(three nutritionists and one nurse)"],
    (8, 0): ["Funding"],
    (8, 1): ["No external funding."],
    (9, 0): ["Target journal"],
    (9, 1): ["Nutrition (Elsevier)"],
}

SIGN = ["MSc. Immer Elías Cuellar Rodríguez", f"Chair, {COMMITTEE}", UNI]

src, dst = sys.argv[1], sys.argv[2]
d = docx.Document(src)
for i, texts in P.items():
    put(d.paragraphs[i], texts)
t0 = d.tables[0]
for (r, c), texts in T.items():
    put(t0.rows[r].cells[c].paragraphs[0], texts)
sig = [p for p in d.tables[1].rows[0].cells[0].paragraphs if p.text.strip()]
for p, t in zip(sig, SIGN):
    put(p, [t])
d.core_properties.language = "en-US"
d.save(dst)

# report any paragraph that still looks Spanish
left = [p.text for p in d.paragraphs if any(w in p.text for w in (" el ", " la ", " de los ", " que "))]
for t in d.tables:
    for row in t.rows:
        for cell in row.cells:
            left += [p.text for p in cell.paragraphs if any(w in p.text for w in (" el ", " la ", " de los "))
                     and "original title" not in p.text]
print("possible untranslated:", left)
