from datetime import datetime, timedelta

def datum_en_terug():
    nu = datetime.now()
    terug = nu + timedelta(days=14)
    return nu.strftime("%Y-%m-%d %H:%M:%S"), terug.strftime("%Y-%m-%d %H:%M:%S")