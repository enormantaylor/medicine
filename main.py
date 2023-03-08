pairs = [
    {"warfarin", "ibuprofen"},
    {"dayquil", "tylenol"},
    {"fluoxetine", "aspirin"},
    {"fluoxetine", "ibuprofen"},
    {"fluoxetine", "naproxen"},
    {"fluoxetine", "diclofenac"},
    {"fluoxetine", "celecoxib"},
    {"aronix", "Nitrostat"},
    {"Liberize", "Nitrostat"},
    {"Nipatra", "Nitrostat"},
    {"Revatio", "Nitrostat"},
    {"Grandipam", "Nitrostat"},
    {"aronix", "NitroMist"},
    {"Liberize", "NitroMist"},
    {"Nipatra", "NitroMist"},
    {"Revatio", "NitroMist"},
    {"Grandipam", "NitroMist"},
    {"Liberize", "Adempas"},
    {"Nipatra", "Adempas"},
    {"Revatio", "Adempas"},
    {"Grandipam", "Adempas"},
    {"Augmentin", "Rheumatrex"},
    {"Augmentin", "Trexall"},
    {"Augmentin", "Amethopterin",
    {"Augmentin", "MTX"},
    {"Augmentin", "Warfarin"},
    {"Augmentin", "Coumadin"},
    {"Augmentin", "Jantoven"},
    {"Augmentin", "MTX"}


]

medicine1 = input("input medicine one: ")
medicine2 = input("input medicine two: ")

if {medicine1,medicine2} in pairs:
    print("please do not take these together or consult a doctor")
else:
    print("there is no evidence that these cannot be taken together, ask your doctor for more information ")