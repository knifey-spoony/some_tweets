from datetime import datetime

s4sv = """20220130    TEST
20220131    I bet I'm not the only one who is saddest in January. That's true for many reasons, some of which are unrelated to weather. Of course it's also because we're in the northern hemisphere. When I tell this joke in Sydney, I'm like: "I bet I'm not... saddest in July..."
20220201    Infinite loops. Amirite?"""

def now_obj2str(dt_obj):
    return str(dt_obj.year) + str(dt_obj.month) + str(dt_obj.day)


def nowinutc():
    ###THIS IS TIMEZONE DEPENDENT
    return datetime.now()

def spacesepstr2datestrdict(sss):
    dsd = {}
    for line in sss.split('\n'):
        d_s, text = line.strip().split('    ')
        dsd[d_s] = text 

    return dsd

def main(sss):
    now_obj = nowinutc()
    now_s = now_obj2str(now_obj)

    text_now_l = []
    dsd = spacesepstr2datestrdict(sss)
    for d_s, txt in dsd.items():
        if d_s == now_s:
            text_now_l.append(txt)

    return text_now_l







if __name__ == "__main__":
    main(s4sv)

