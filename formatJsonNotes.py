import ast

def format_title(title):
  return '<h%d>%s</h%d>'%(3,title,3)

def format_content(json):
  content = ''
  contentJson = json['content']
  sections = []
  index = 1

  while str(index) in contentJson:
    sections.append(contentJson[str(index)])
    index += 1

  for section in sections:
    content = '%s%s'%(content,format_title(section['title']))

  return content

if __name__ == '__main__':
  import sys
  name = sys.argv[1]
  f = open(name,'r')
  jsonString = f.readline()
  json = ast.literal_eval(jsonString)
  f.close()
  content = format_content(json)
  print(content)
  

