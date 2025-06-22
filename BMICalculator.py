##!/usr/bin/env python3
import sys

def get_numeric_input(prompt, input_type=float):
    """
    Fragt den Benutzer nach einer numerischen Eingabe, validiert sie
    und gibt sie zurück. Wiederholt die Abfrage bei ungültiger Eingabe.

    Args:
        prompt (str): Die anzuzeigende Eingabeaufforderung.
        input_type (type): Der erwartete Datentyp (int oder float).

    Returns:
        int or float: Die validierte numerische Eingabe des Benutzers.
    """
    while True:
        try:
            # Ersetze Komma durch Punkt für Dezimalzahlen, falls nötig
            value_str = input(prompt).replace(',', '.')
            value = input_type(value_str)
            if value <= 0:
                print("Fehler: Der Wert muss größer als 0 sein.")
            else:
                return value  # Gültige Eingabe, Schleife verlassen und Wert zurückgeben
        except ValueError:
            # Fehler bei der Typumwandlung
            print(f"Fehler: Bitte geben Sie eine gültige {'ganze Zahl' if input_type == int else 'Zahl'} ein.")
        except Exception as e:
            # Fange andere mögliche Fehler ab
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
            # Beende das Programm bei unerwarteten Fehlern, um Endlosschleifen zu vermeiden
            sys.exit(1)

def calculate_bmi(gewicht, groesse):
    """Berechnet den Body-Mass-Index (BMI)."""
    if groesse <= 0:
        # Ungültig, wenn Größe 0 oder negativ ist
        # Sollte durch get_numeric_input bereits verhindert werden, aber sicher ist sicher
        return None
    # BMI = Gewicht (kg) / (Größe (m) * Größe (m))
    # ** ist der Potenzierungsoperator in Python
    return gewicht / (groesse ** 2)

def interpret_bmi(bmi):
    """Interpretiert den BMI-Wert für Erwachsene."""
    if bmi is None:
        return "BMI konnte nicht berechnet werden (ungültige Eingabe)."
    elif bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25: # 18.5 <= bmi < 25
        return "Normalgewicht"
    elif bmi < 30: # 25 <= bmi < 30
        return "Übergewicht"
    else: # bmi >= 30
        return "Starkes Übergewicht (Adipositas)"

def calculate_optimal_weight_range(groesse):
    """Berechnet den optimalen Gewichtsbereich basierend auf einem gesunden BMI."""
    if groesse <= 0:
        return None # Kein optimales Gewicht für ungültige Größe

    # Definiere den "gesunden" BMI-Bereich (Normalgewicht)
    BMI_MIN_NORMAL = 18.5
    BMI_MAX_NORMAL = 24.9 # Oft wird < 25 verwendet, 24.9 ist präziser für die Obergrenze

    # Berechne das minimale und maximale Gewicht für diesen BMI-Bereich
    # Formel umgestellt: Gewicht = BMI * Größe²
    min_optimal_weight = BMI_MIN_NORMAL * (groesse ** 2)
    max_optimal_weight = BMI_MAX_NORMAL * (groesse ** 2)

    return (min_optimal_weight, max_optimal_weight)

# Hauptteil des Programms
# Dieser Block wird nur ausgeführt, wenn das Skript direkt gestartet wird
if __name__ == "__main__":
    print("--- BMI Rechner ---")

    # Eingaben abfragen mit Validierung durch die Hilfsfunktion
    # Das Alter wird für die BMI-Berechnung selbst nicht benötigt, aber für Kontext
    alter = get_numeric_input("Bitte geben Sie Ihr Alter ein: ", int)
    gewicht = get_numeric_input("Bitte geben Sie Ihr Gewicht in Kilogramm ein (z.B. 75.5): ", float)
    groesse = get_numeric_input("Bitte geben Sie Ihre Größe in Metern ein (z.B. 1.80): ", float)

    # BMI berechnen
    bmi_wert = calculate_bmi(gewicht, groesse)

    # Optimalgewichtsbereich berechnen
    optimal_gewicht_bereich = calculate_optimal_weight_range(groesse)

    # Ergebnisse ausgeben
    print("\n--- Ihre Daten ---")
    print(f"Alter: {alter} Jahre")
    print(f"Gewicht: {gewicht:.1f} kg") # Formatierung auf 1 Nachkommastelle
    print(f"Größe: {groesse:.2f} m")   # Formatierung auf 2 Nachkommastellen

    print("\n--- Ergebnisse ---")
    if bmi_wert is not None:
        # Gib den berechneten BMI aus
        print(f"Ihr Body-Mass-Index (BMI) beträgt: {bmi_wert:.2f}") # Formatierung auf 2 Nachkommastellen

        # Interpretation des aktuellen BMI ausgeben
        interpretation = interpret_bmi(bmi_wert)
        print(f"Interpretation (Standard für Erwachsene): {interpretation}")
    else:
        # Fehlermeldung, falls BMI nicht berechnet werden konnte
        print("BMI konnte aufgrund ungültiger Eingaben nicht berechnet werden.")

    # Gib den Optimalgewichtsbereich aus, falls berechenbar
    if optimal_gewicht_bereich is not None:
        min_gewicht, max_gewicht = optimal_gewicht_bereich
        print(f"\nIhr Optimalgewicht (für einen BMI zwischen 18.5 und 24.9) liegt etwa zwischen: "
              f"{min_gewicht:.1f} kg und {max_gewicht:.1f} kg.")
    else:
        # Fehlermeldung, falls Optimalgewicht nicht berechnet werden konnte
        print("\nOptimalgewicht konnte aufgrund ungültiger Größe nicht berechnet werden.")


    print("\n--- Hinweise ---")
    print("- Die BMI-Interpretation und das Optimalgewicht gelten primär für Erwachsene.")
    print("- Für Kinder, Jugendliche, Schwangere, Stillende sowie sehr muskulöse Menschen ist der BMI nur bedingt aussagekräftig.")
    print("- Bei Gesundheitsfragen konsultieren Sie bitte immer einen Arzt.")
