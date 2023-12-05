import time

def afficher_heure(heure, mode_12h=False):
    if mode_12h:
        am_pm = "AM"
        if heure[0] >= 12:
            am_pm = "PM"
        heure[0] = heure[0] % 12
        if heure[0] == 0:
            heure[0] = 12
        heure_format = "{:02d}:{:02d}:{:02d} {}".format(heure[0], heure[1], heure[2], am_pm)
    else:
        heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format, end='\r')  
    return heure_format


def regler_heure(heure, heures, minutes, secondes):
    heure = (heures, minutes, secondes)
    return heure


def regler_alarme(alarme, heures, minutes, secondes):
    alarme = (heures, minutes, secondes)
    return alarme

def choisir_mode_affichage():
    while True:
        mode = input("Choisissez le mode d'affichage (12h ou 24h): ").lower()
        if mode in ["12h", "24h"]:
            return mode == "12h"
        else:
            print("Veuillez choisir entre '12h' et '24h'.")


def verifier_alarme(heure, alarme):
    if heure == alarme:
        print("\nAlarme! Il est maintenant {}".format(afficher_heure(heure, mode_12h)))
        return True
    return False


def main():
    heure = (16, 30, 0)  
    alarme = (0, 0, 0)  

    global mode_12h
    mode_12h = choisir_mode_affichage()

    try:
        while True:
            afficher_heure(heure, mode_12h)
            if verifier_alarme(heure, alarme):
                break
            time.sleep(1)  
            heure = (heure[0], heure[1], heure[2] + 1)  
            if heure[2] == 60:
                heure = (heure[0], heure[1] + 1, 0)
            if heure[1] == 60:
                heure = (heure[0] + 1, 0, 0)
            if heure[0] == 24:
                heure = (0, 0, 0)
    except KeyboardInterrupt:
        print("\nProgramme arrêté par l'utilisateur.")

if __name__ == "__main__":
    main()
