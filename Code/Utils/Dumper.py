import sys

def get_type(line):
    url_type = "unknown"
    if "apps/details?id=" in line:
        url_type = "app"
    else:
        if "apps/developer?id=" in line:
            url_type = "developer"
        else:
            url_type = "page"
    print("URL: '" + line + "', type: '" + url_type + "'")
    return url_type
    pass

def write_list(filename, lines):
    file = open(filename, "w")
    for line in lines:
        file.write(line + "\n")
    print("Save to file '" + filename + "' (" + str(len(lines)) + " lines)")
    file.close()

def make():
    file_name = sys.argv[1]
    file = open(file_name, "r")

    apps = []
    developers = []
    pages = []

    total = 0
    header = True

    for line in file:
        if header:
            print("HEADER: " + file.readline().rstrip())
            header = False
        else:
            conv_line = line.rstrip()
            line_type = get_type(conv_line)
            total += 1
            if line_type == "app":
                apps.append(conv_line)
            if line_type == "developer":
                developers.append(conv_line)
            if line_type == "page":
                pages.append(conv_line)

    print("Total: " + str(total))
    print("Apps: " + str(len(apps)))
    print("Developers: " + str(len(developers)))
    print("Pages: " + str(len(pages)))

    write_list("apps.csv", apps)
    write_list("developers.csv", developers)
    write_list("pages.csv", pages)
make()
