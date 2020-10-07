import os
import csv
import json
import shutil
from pathlib import Path
from python_loc_counter import LOCCounter

# Caminho dos arquivos .CSV:
CAMINHO_CSV = "analise"


# Verifica se um repositorio foi analisado:
def analisado(nameWithOwner, csvfile):
    try:
        with open(csvfile, "r") as f:
            for line in f.readlines():
                if nameWithOwner in line:
                    return True
    except Exception as e:
        pass
    return False


# Obtem o LOC, BLOC e CLOC de um repositorio
def analisar(dir, lang):
    result = {'source_loc': 0, 'single_comments_loc': 0, 'single_docstring_loc': 0,
              'double_docstring_loc': 0, 'total_comments_loc': 0, 'blank_loc': 0, 'total_line_count': 0}
    try:
        if os.path.isdir("%s/.git" % dir):
            os.system('rmdir /S /Q "%s/.git"' % dir)
        for source_path in Path(dir).rglob("*.%s" % lang):
            try:
                src_path = str(source_path)
                counter = LOCCounter(src_path)
                loc_data = counter.getLOC()
                for key in loc_data:
                    if key in result:
                        result[key] += loc_data[key]
                    else:
                        result[key] = loc_data[key]
                print(loc_data)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    return result


# Converte as linhas de um arquivo CSV para dicts
def lerCSV(file):
    reader = csv.DictReader(open(file, encoding="utf-8"))
    for row in reader:
        for attr in row:
            try:  # Tenta converter o atributo de json para um objeto
                objAttr = json.loads(row[attr].replace("'", '"'))
                row[attr] = objAttr
            except ValueError:
                pass
        yield row


# Adiciona um repositorio ao csv
def append_csv(file, row):
    existe = os.path.isfile(file)
    try:
        with open(file, 'a+') as f:
            w = csv.DictWriter(f, row.keys())
            if not existe:
                w.writeheader()
            w.writerow(row)
    except Exception as e:
        print(e)


def main():
    for root, dirs, files in os.walk("csv", topdown=False):
        for file in [os.path.join(root, name) for name in files if name.endswith(".csv")]:
            for r in lerCSV(file):
                erros = 0
                try:
                    fullname = r["nameWithOwner"]
                    name = fullname.split("/")[1]
                    lang = r["languages"]["edges"][0]["node"]["name"]
                    if analisado(fullname, "%s/%s.csv" % (CAMINHO_CSV, lang)):
                        print("%s ja foi analisado" % (fullname))
                        continue
                    dir = "repos/%s/%s" % (lang.lower(), name)
                    if not os.path.isdir(dir):
                        os.system("git clone %s %s --depth=1" %
                                  (r["url"], dir))
                    analise = analisar(dir, lang)
                    r["loc"] = analise["source_loc"]
                    r["cloc"] = analise["total_comments_loc"]
                    r["bloc"] = analise["blank_loc"]
                    r["linguagem"] = lang
                    r["stargazers"] = r["stargazers"]["totalCount"]
                    r["releases"] = r["releases"]["totalCount"]
                    del r["languages"]
                    append_csv("analise/%s.csv" % lang, r)
                except Exception as e:
                    erros += 1
                    print(e)


if __name__ == "__main__":
    main()
