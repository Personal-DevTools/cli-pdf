import argparse
from lib import fileCommon, readFieldnames

parser = argparse.ArgumentParser(description="A PDF CLI Tool")

parser.add_argument('-i', '--input', type=str, required=True, help='input File')
parser.add_argument('-o', '--output', type=str, help='output')
parser.add_argument('-rf', '--readfieldnames', action='store_true', help='output')

# # Argumente parsen
args = parser.parse_args()


if args.input:
    fileCommon.check_exits_file(args.input)
    fileCommon.is_pdf(args.input)

if args.readfieldnames: 
    if args.output:
        fields = readFieldnames.readFieldnames(args.input)
        readFieldnames.saveFieldnames(fields, args.output)
    else: 
        readFieldnames.readFieldnames(args.input)
 

# # Zugriff auf die übergebenen Parameter
# print(f"Eingabedatei: {args.input}")
# print(f"Ausgabedatei: {args.output}")

# # Hier kannst du dann den Logikteil deines Programms hinzufügen
# # Beispiel: Datei öffnen, lesen und verarbeiten

