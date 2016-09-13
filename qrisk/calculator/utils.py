from qrisk.calculator.models import QUser, QUserInfo
from py_qrisk import calcFemRaw


def int_from_bool(my_bool):
    return 1 if my_bool is True else 0


def calc_bmi(w, h):
    if not h or not w:
        res = 0
    else:
        res = (w / h) / h
    return float(res)


def calculate(user):
    return calc_fem(user) if user.sex == QUser.FEMALE else calc_mal(user)


def calc_mal(user):
    raise NotImplementedError('Method or function hasn\'t been implemented yet.')


def calc_fem(user):
    info = user.info
    af = int_from_bool(info.atrial_fibrillation)
    ra = int_from_bool(info.rheumatoid_arthritis)
    renal = int_from_bool(info.kidney_disease)
    treatedhyp = int_from_bool(info.blood_pressure_treat)
    t1 = 1 if info.diabetes_status == QUserInfo.T1 else 0
    t2 = 1 if info.diabetes_status == QUserInfo.T2 else 0
    bmi = calc_bmi(info.weight, info.height)
    ethrisk = dict(QUser.ETHN_CHOICES).keys().index(user.ethnicity) + 1
    rati = float(int_from_bool(info.rheumatoid_arthritis))
    smoke_cat = dict(QUserInfo.SMOKER_CHOICES).keys().index(info.smoking_status) + 1

    import pdb; pdb.set_trace()

    a = calcFemRaw(user.age, af, ra, renal, treatedhyp, t1, t2, bmi, ethrisk,
                   info.heart_attacked_relative, rati, info.blood_pressure, smoke_cat, 1.0)

    return a
