def touples(my_dict):
    touple =()
    for key,data in my_dict.iteritems():
        # print key, " = ", data
        touple += key, data
        # touple += data
    print touple


my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print touples(my_dict)

