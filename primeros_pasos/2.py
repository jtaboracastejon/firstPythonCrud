
#----------------------------------------------------------------------------------
reading_file = open("Desktop/hola1.sql", "r")

new_file_content = ""
for line in reading_file:
  stripped_line = line.strip()
  new_line = stripped_line.replace("Z'", "'").replace("MOCKDATA","rental")
  new_file_content += new_line + "\n"
reading_file.close()

writing_file = open("Desktop/2/hola1replaced.sql", "w")
writing_file.write(new_file_content)
writing_file.close()
