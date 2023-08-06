import os, json, re, win32gui, win32con, sys

# Get path of working directory
def get_path():
    if getattr(sys, 'frozen', False):
        main_path = os.path.dirname(sys.executable)
        return main_path
    elif __file__:
        main_path = os.path.dirname(__file__)
        return main_path

main_path = os.path.join(get_path(),"Data")

# MAXIMIZE TERMINAL FOR SEVERAL OPERATIONS
def maximize():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# RENAMING PETNAME IN APP_NAMES FILE
def do_changes(app,petname):
    with open((os.path.join(main_path,"app_names.json")),"r") as file:
        data = json.load(file)
        data.pop(app)
        change = {app:petname.lower()}
        data.update(change)
    with open((os.path.join(main_path,"app_names.json")),"w") as file1:
        json.dump(data,file1,indent=4)

# CHANGE PRE / SEC NAME IN DATA FILE
def pre_change():
    file = open((os.path.join(main_path,"app_names_temp.json")),"r")
    data_file_read = open((os.path.join(main_path,"data.json")),"r")
    data_read = json.load(data_file_read)
    data_file = json.load(file)
    keys_file = list(data_file.keys())
    values_file = list(data_file.values())
    for app2 in keys_file:
        if data_file[app2] != "":
            position = keys_file.index(app2)
            app=values_file[position]
            #print('"'+app2+'"','"'+app+'"')
            try:
                data_read[app] = data_read.pop(app2)
            except:
                pass
            #del data_r[app2]
    with open((os.path.join(main_path,"data.json")),"a+") as f:
        g = open((os.path.join(main_path,"data.json")),"r+")
        g.truncate(0)
        json.dump(data_read,f,indent=4)

# CHANGES IN MAIN DATA FILE (PETNAME)
def change_in_data(app,petname):
    with open((os.path.join(main_path,"data.json")),"r") as file:
        data = json.load(file)
    try:
        data[petname] = data.pop(app)
    except: pass
    with open((os.path.join(main_path,"data.json")),"w") as file1:
        json.dump(data,file1,indent=4)

# REVIEW CHANGES IN APP_NAMES FILE
def modify():
    with open((os.path.join(main_path,"app_names.json")),"r") as file:
        data = json.load(file)
        keys = list(data.keys())
        values = list(data.values())
        for petname in values:
            if petname != "":
                position = values.index(petname)
                app = keys[position]
                #print(app,petname)
                change_in_data(app,petname)
                
# CHANGE ALL PETNAMES TO DEFAULT APP NAMES
def default(output=True):
    if output:
        print("RESTORING DEFAULT APP NAMES")
    file1 = open((os.path.join(main_path,"app_names.json")),"r")
    data1 = json.load(file1)
    keys = list(data1.keys())
    values = list(data1.values())
    file2 = open((os.path.join(main_path,"app_names.json")),"r")
    data2 = json.load(file2)
    for petname in values:
        if petname != "":
            position = values.index(petname)
            app=keys[position]
            #print(app+" "+petname)
            change = {app:app}
            data2.update(change)
    file3 = open((os.path.join(main_path,"app_names.json")),"w")
    json.dump(data2,file3,indent=4)
    if output:
        print("DONE.")

# EXECUTE CHANGES IN DATA FILE
def check_new_name():
    file = open((os.path.join(main_path,"app_names.json")),"r")
    app_temp = open((os.path.join(main_path,"app_names_temp.json")),"r")
    data_temp = json.load(app_temp)
    data = json.load(file)
    keys = list(data.keys())
    values = list(data.values())
    for app2 in values:
        if app2 != "":
            position = values.index(app2)
            app = keys[position]
            change = {app2:app}
            data_temp.update(change)
    with open((os.path.join(main_path,"app_names_temp.json")),"a+") as f:
        g = open((os.path.join(main_path,"app_names_temp.json")),"r+")
        g.truncate(0)
        json.dump(data_temp,f,indent=4)

# DEPENDENCY OF (3)
def edit_things_cli(count,current_name,petname):
    with open((os.path.join(main_path,"app_names.json")),"r") as app_file:
        data = json.load(app_file)
    for app_name in data:
        if current_name == app_name:
            change = {current_name:petname}
            data.update(change)
            with open((os.path.join(main_path,"app_names.json")),"a+") as f:
                g = open((os.path.join(main_path,"app_names.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
                if count == None:
                    count = 1
                print(str(count)+". "+current_name.upper()+" IS NOW "+petname.upper())

# SORT MULTIPLE CHANGES OF APPS VIA CLI - 3
def do_changes_cli(self):
    if "," in self:
        count = 0
        splited=self.split(",")
        for i in splited:
            j = i.strip()
            if j != "":
                count += 1
                split2 = j.split(">")
                current_name = (split2[0]).strip()
                petname = (split2[1]).strip()
                edit_things_cli(count,current_name,petname)
    else:
        splited = self.split(">")
        # print(splited)
        current_name = (splited[0]).strip()
        petname = (splited[1]).strip()
        edit_things_cli(1,current_name,petname)

# FETCH ALL NEW APPS
def update(output=True):
    maximize()
    os.system("mode 800")
    if output:
        print("FETCHING ALL NEW APPS (if any)")
    os.system("powershell -command "+'"'+"get-StartApps | Out-File -encoding ASCII -Filepath "+"'"+(os.path.join(main_path,"reference.txt"))+"'"+'"')
    os.system("mode 100")
    if output:
        print("UPDATING THE LIST, THIS MAY TAKE TIME...")
    with open((os.path.join(main_path,"reference.txt")),"r") as fd:
        lines = fd.readlines()
    line = []
    with open((os.path.join(main_path,"reference.txt")),"w") as fp:
        for number, line in enumerate(lines):
            if number not in [0, 1,2]:
                fp.write(line)
    with open((os.path.join(main_path,"reference.txt")),"r") as f, open((os.path.join(main_path,"reference_temp.txt")),"w+") as outfile:
        for i in f.readlines():
            if not i.strip():
                continue
            if i:
                outfile.write(i)
    try: os.remove(os.path.join(main_path,"reference_temp.txt"))
    except: pass
    dictionary ={}
    with open((os.path.join(main_path,"data.json")),"w") as outfile:
        json.dump(dictionary, outfile)
    file1 = open(os.path.join(main_path,'reference.txt'),'r')
    Lines = file1.readlines()
    for line in Lines:
        line1= line.strip()
        index = line1.find('  ')
        # HERE line1[:index] is the APP-NAME
        # HERE line1[index:] is the APP-ID.
        app_name = line1[:index]
        app_id = (line1[index:]).strip()
        is_digit = app_name[:1].isdigit()
        with open ((os.path.join(main_path,"data.json")),"r") as f:
                data = json.load(f)
        if is_digit == (False):
            val=(re.compile(r'[^a-z-&]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open((os.path.join(main_path,"data.json")),"a+") as f:
                g = open((os.path.join(main_path,"data.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
        elif is_digit == (True):
            val=(re.compile(r'[^a-z-&^0-9+]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open((os.path.join(main_path,"data.json")),"a+") as f:
                g = open((os.path.join(main_path,"data.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
    if output:
        print("WRITING APP NAMES")
    with open((os.path.join(main_path,"app_names.json")),"r") as old_AF:
        old = json.load(old_AF)
    with open((os.path.join(main_path,"app_names_temp.json")),"w+") as temp_af:
        json.dump(old,temp_af,indent=4)
    dictionary ={}
    json_object = json.dumps(dictionary, indent = 4)
    with open((os.path.join(main_path,"app_names.json")),"w") as outfile:
        outfile.write(json_object)
    with open((os.path.join(main_path,"data.json")),"r") as app_file:
        data1 = json.load(app_file)
    with open((os.path.join(main_path, "app_names.json")),"r") as file:
        data = json.load(file)
    for app_name in data1:
        change = {app_name:""}
        data.update(change)
        with open((os.path.join(main_path,"app_names.json")),"a+") as f:
            g = open((os.path.join(main_path,"app_names.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
    with open((os.path.join(main_path,"app_names_temp.json")),"r") as file:
        data = json.load(file)
        values = list(data.values())
        keys = list(data.keys())
    for petname in values:
        if petname != "":
            position = values.index(petname)
            app_old=keys[position]
            # print(str(app_old)+" changed to "+str(petname))
            do_changes(app_old,petname)
    check_new_name()
    if output:
        print("LIST UPDATED.")

# SETUP FILES - 1
def check_app_names():
    try:
        file1 = open(os.path.join(main_path,'data.json'),'r')
    except: pass
    print()
    print("PREPARING FOR INPUTS (JUST ONCE)")
    dictionary ={}
    with open((os.path.join(main_path,"app_names.json")),"w") as outfile:
        json.dump(dictionary, outfile)
    with open((os.path.join(main_path,"data.json")),"r") as app_file:
        data = json.load(app_file)
    data1 = json.load(file1)
    for app_name in data1:
        change = {app_name:""}
        data.update(change)
        with open((os.path.join(main_path,"app_names.json")),"a+") as f:
            g = open((os.path.join(main_path,"app_names.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
    with open((os.path.join(main_path,"app_names_temp.json")),"w") as outfile:
        json.dump(dictionary, outfile)
