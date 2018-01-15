import re

import language_check

tool = language_check.LanguageTool('en-GB')
output = open("comments.csv", "w+")
output.write("Line No, Comments, Suggestions\n")
line_no = []
fileName = "test.rb"
fileType = "Ruby"
i = 0

if fileType == "Java" or fileType == "C++":
    l_no = 0
    # Extracting single line comments of C++ or Java style.
    with open(fileName, 'r') as file:
        for line in file:
            l_no += 1
            if re.search("/\*", line):
                line_no.append(l_no)
            match = re.search("//.*", line)
            if match is not None:
                match = match.group()
                comment = re.search("[^//][A-Za-z0-9].*", match).group()
                matches = tool.check(comment)
                if len(matches) > 0:
                    suggestion = language_check.correct(comment, matches)
                    suggestion = str(l_no) + "," + '"' + comment + '"' + "," + '"' + suggestion + '"' + "\n"
                    output.write(suggestion)

    # Extracting multi line comments of c++ or Java style
    with open(fileName, 'r') as file:
        text = file.read()
        matches = re.findall(r'/\*.*?\*/', text, re.DOTALL)
        for x in matches:
            x = x.replace("/*", "")
            x = x.replace("*/", "")
            x = x.replace("*", "")
            x = x.replace("\n", " ")
            x = re.sub('\s+', ' ', x)
            matches = tool.check(x)
            if len(matches) > 0:
                suggestion = language_check.correct(x, matches)
                suggestion = str(line_no[i]) + "," + '"' + x + '"' + "," + '"' + suggestion + '"' + "\n"
                output.write(suggestion)
                i += 1


if fileType == "Python":
    l_no = 0
    # Extracting single line comments of Python style.
    with open(fileName, 'r') as file:
        for line in file:
            l_no += 1
            if re.search("\"\"\"", line):
                line_no.append(l_no)
            match = re.search("#.*", line)
            if match is not None:
                match = match.group()
                comment = re.search("[^#][A-Za-z0-9].*", match).group()
                matches = tool.check(comment)
                if len(matches) > 0:
                    suggestion = language_check.correct(comment, matches)
                    suggestion = str(l_no) + "," + '"' + comment + '"' + "," + '"' + suggestion + '"' + "\n"
                    output.write(suggestion)

    # Extracting multi line comments of Python style
    with open(fileName, 'r') as file:
        text = file.read()
        matches = re.findall(r'\"\"\".*?\"\"\"', text, re.DOTALL)
        for x in matches:
            x = x.replace("\"\"\"", "")
            x = x.replace("\n", " ")
            x = re.sub('\s+', ' ', x)
            matches = tool.check(x)
            if len(matches) > 0:
                suggestion = language_check.correct(x, matches)
                suggestion = str(line_no[i % 2]) + "," + '"' + x + '"' + "," + '"' + suggestion + '"' + "\n"
                output.write(suggestion)
                i += 1

if fileType == "Php":
    l_no = 0
    # Extracting single line comments of php style.
    with open(fileName, 'r') as file:
        for line in file:
            l_no += 1
            if re.search("/\*", line):
                line_no.append(l_no)
            match = re.search("//.*", line)
            if match is not None:
                match = match.group()
                comment = re.search("[^//][A-Za-z0-9].*", match).group()
                matches = tool.check(comment)
                if len(matches) > 0:
                    suggestion = language_check.correct(comment, matches)
                    suggestion = str(l_no) + "," + '"' + comment + '"' + "," + '"' + suggestion + '"' + "\n"
                    output.write(suggestion)

                match = re.search("#.*", line)
                if match is not None:
                    match = match.group()
                    comment = re.search("[^#][A-Za-z0-9].*", match).group()
                    matches = tool.check(comment)
                    if len(matches) > 0:
                        suggestion = language_check.correct(comment, matches)
                        suggestion = str(l_no) + "," + '"' + comment + '"' + "," + '"' + suggestion + '"' + "\n"
                        output.write(suggestion)

    # Extracting multi line comments of php style
    with open(fileName, 'r') as file:
        text = file.read()
        matches = re.findall(r'/\*.*?\*/', text, re.DOTALL)
        for x in matches:
            x = x.replace("/*", "")
            x = x.replace("*/", "")
            x = x.replace("*", "")
            x = x.replace("\n", " ")
            x = re.sub('\s+', ' ', x)
            matches = tool.check(x)
            if len(matches) > 0:
                suggestion = language_check.correct(x, matches)
                suggestion = str(line_no[i]) + "," + '"' + x + '"' + "," + '"' + suggestion + '"' + "\n"
                output.write(suggestion)
                i += 1

if fileType == "Ruby":
    l_no = 0
    # Extracting single line comments of ruby style.
    with open(fileName, 'r') as file:
        for line in file:
            l_no += 1
            if re.search("(=begin)", line):
                line_no.append(l_no)
            match = re.search("#.*", line)
            if match is not None:
                match = match.group()
                comment = re.search("[^#][A-Za-z0-9].*", match).group()
                matches = tool.check(comment)
                if len(matches) > 0:
                    suggestion = language_check.correct(comment, matches)
                    suggestion = str(l_no) + "," + '"' + comment + '"' + "," + '"' + suggestion + '"' + "\n"
                    output.write(suggestion)

    # Extracting multi line comments of ruby style
    with open(fileName, 'r') as file:
        text = file.read()
        matches = re.findall(r'=begin.*?=end', text, re.DOTALL)
        for x in matches:
            x = x.replace("=begin", "")
            x = x.replace("=end", "")
            x = x.replace("\n", " ")
            x = re.sub('\s+', ' ', x)
            matches = tool.check(x)
            if len(matches) > 0:
                suggestion = language_check.correct(x, matches)
                suggestion = str(line_no[i]) + "," + '"' + x + '"' + "," + '"' + suggestion + '"' + "\n"
                output.write(suggestion)
                i += 1

output.close()
