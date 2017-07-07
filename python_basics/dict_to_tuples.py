my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
arr = []
for key, value in my_dict.iteritems():
    arr.append((key,value))
print arr