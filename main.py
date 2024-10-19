import argparse
from lib import fileCommon, readFieldnames, rename

parser = argparse.ArgumentParser(description="A PDF CLI Tool")

parser.add_argument('-i', '--input', type=str, required=True, help='input File')
parser.add_argument('-o', '--output', type=str, help='output')
parser.add_argument('-rf', '--readfieldnames', action='store_true', help='read fieldnames')
parser.add_argument('-rn', '--renamefieldnames', type=str, help='rename fieldnames')

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
 
if args.renamefieldnames:
    if not args.output:
        print(f"Required Output pdf File")
        exit()
    fileCommon.check_exits_file(args.input)
    fileCommon.is_pdf(args.input)
    fileCommon.is_json(args.renamefieldnames)
    rename.renameFields(args.input, args.renamefieldnames , args.output)
     
 

