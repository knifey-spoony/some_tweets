from datetime import datetime, timezone
from collections import defaultdict

s4sv = """20220130    TEST
20220131    I bet I'm not the only one who is saddest in January. That's true for many reasons, some of which are unrelated to weather. Of course it's also because we're in the northern hemisphere. When I tell this joke in Sydney, I'm like: "I bet I'm not... saddest in July..."
20220201    Infinite loops. Amirite?"""
 
def spacesepstr2dateobjdefdict(sss):
    dsd = defaultdict(list)
    for line in sss.split('\n'):
        d_s, text = line.strip().split('    ')
        date_obj = datetime.strptime(d_s, "%Y%m%d").date()
        dsd[date_obj].append(text)

    return dsd

def spacesepstr2todaystext_l(sss):
    date_obj = datetime.now(timezone.utc).date()
    dsd = spacesepstr2dateobjdefdict(sss)
    return dsd[date_obj]



if __name__ == "__main__":
    print(spacesepstr2todaystext_l(s4sv))

