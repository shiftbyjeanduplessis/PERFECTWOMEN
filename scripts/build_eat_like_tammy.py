from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
import os
W,H=A4; M=10*mm
TEAL=HexColor('#0AA8B5'); TD=HexColor('#07687B'); CORAL=HexColor('#FF5157'); YELLOW=HexColor('#FFD526'); NAVY=HexColor('#0A4B67'); INK=HexColor('#26424F'); GREY=HexColor('#6F858E'); LIGHT=HexColor('#BFE7EA'); PB=HexColor('#E8F9FA'); PC=HexColor('#FFF0EF'); PY=HexColor('#FFF9D6'); CREAM=HexColor('#FFFCF4'); WHITE=white
OUT='downloads/Perfect_Women_Eat_Like_Tammy_ELEVATED-compressed.pdf'
os.makedirs('downloads',exist_ok=True)
def rr(c,x,y,w,h,r=3*mm,fill=None,stroke=None,lw=1):
 c.saveState();
 if fill is not None:c.setFillColor(fill)
 if stroke is not None:c.setStrokeColor(stroke)
 c.setLineWidth(lw); c.roundRect(x,y,w,h,r,fill=1 if fill is not None else 0,stroke=1 if stroke is not None else 0); c.restoreState()
def tx(c,x,y,s,size=10,font='Helvetica',color=INK): c.setFillColor(color); c.setFont(font,size); c.drawString(x,y,s)
def ctr(c,x,y,w,s,size=10,font='Helvetica-Bold',color=INK): c.setFillColor(color); c.setFont(font,size); c.drawCentredString(x+w/2,y,s)
def right(c,x,y,s,size=7,font='Helvetica-Bold',color=GREY): c.setFillColor(color); c.setFont(font,size); c.drawRightString(x,y,s)
def lines(text,font,size,maxw):
 out=[]; cur=''
 for word in text.split():
  t=(cur+' '+word).strip()
  if stringWidth(t,font,size)<=maxw: cur=t
  else:
   if cur: out.append(cur)
   cur=word
 if cur: out.append(cur)
 return out
def wrap(c,text,x,y,w,size=8,font='Helvetica',color=INK,leading=None,max_lines=None):
 if leading is None: leading=size*1.2
 ls=lines(text,font,size,w)
 if max_lines: ls=ls[:max_lines]
 c.setFillColor(color); c.setFont(font,size)
 for ln in ls: c.drawString(x,y,ln); y-=leading
 return y
def bg(c,p):
 c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0); c.setStrokeColor(TEAL); c.setLineWidth(2.6); c.roundRect(3*mm,3*mm,W-6*mm,H-6*mm,5*mm,fill=0,stroke=1); right(c,W-7*mm,6*mm,str(p))
def header(c):
 c.setFillColor(YELLOW); c.rect(52*mm,H-14*mm,14*mm,2.4*mm,fill=1,stroke=0); c.rect(W-66*mm,H-14*mm,14*mm,2.4*mm,fill=1,stroke=0); c.setFillColor(TEAL); c.rect(52*mm,H-18*mm,14*mm,2.4*mm,fill=1,stroke=0); c.rect(W-66*mm,H-18*mm,14*mm,2.4*mm,fill=1,stroke=0); ctr(c,0,H-15*mm,W,'PERFECT WOMEN',15,'Helvetica-Bold',CORAL); rr(c,W/2-25*mm,H-27*mm,50*mm,8*mm,2*mm,fill=YELLOW); ctr(c,W/2-25*mm,H-24.5*mm,50*mm,"Let's Do It Together",8.2,'Helvetica-Bold',NAVY)
def title(c,h,s=''):
 ctr(c,M,H-44*mm,W-2*M,h.upper(),24,'Helvetica-Bold',TD)
 if s: rr(c,W/2-48*mm,H-57*mm,96*mm,9*mm,3*mm,fill=CORAL); ctr(c,W/2-48*mm,H-54.2*mm,96*mm,s,8.8,'Helvetica-Bold',WHITE)
def bullet(c,x,y,text,color=TEAL,w=150*mm,size=8.2): c.setFillColor(color); c.circle(x,y+1*mm,1.5*mm,fill=1,stroke=0); wrap(c,text,x+5*mm,y,w,size,'Helvetica',INK,size*1.15,3)
def card(c,x,y,w,h,head,body,fill=WHITE,accent=TEAL): rr(c,x,y,w,h,4*mm,fill=fill,stroke=accent); tx(c,x+4*mm,y+h-11*mm,head,9.2,'Helvetica-Bold',NAVY); wrap(c,body,x+4*mm,y+h-20*mm,w-8*mm,7.7,'Helvetica',INK,9,5)
c=canvas.Canvas(OUT,pagesize=A4)
# cover
c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0); c.setStrokeColor(TEAL); c.setLineWidth(10); c.rect(4*mm,4*mm,W-8*mm,H-8*mm,fill=0,stroke=1); ctr(c,0,H-32*mm,W,'PERFECT WOMEN',24,'Helvetica-Bold',CORAL); rr(c,W/2-34*mm,H-45*mm,68*mm,9*mm,fill=YELLOW); ctr(c,W/2-34*mm,H-42*mm,68*mm,"LET'S DO IT TOGETHER",9,'Helvetica-Bold',NAVY); ctr(c,M,H-88*mm,W-2*M,'EAT LIKE',44,'Helvetica-Bold',TEAL); ctr(c,M,H-126*mm,W-2*M,'TAMMY',49,'Helvetica-Bold',CORAL); ctr(c,M,H-147*mm,W-2*M,'8-WEEK FOOD GUIDE',19,'Helvetica-Bold',TEAL); ctr(c,M,H-160*mm,W-2*M,'with Coach Tammy',11,'Helvetica-Bold',NAVY)
for i,(a,b,col) in enumerate([('CLEAR','PORTIONS',TEAL),('ONE','STARCH',CORAL),('REAL','FOOD',TEAL)]):
 x=M+i*((W-2*M-8*mm)/3+4*mm); bw=(W-2*M-8*mm)/3; rr(c,x,H-220*mm,bw,42*mm,4*mm,fill=col); ctr(c,x,H-194*mm,bw,a,12,'Helvetica-Bold',WHITE); ctr(c,x,H-207*mm,bw,b,12,'Helvetica-Bold',WHITE); rr(c,x,H-220*mm,bw,11*mm,0,fill=YELLOW); ctr(c,x,H-216*mm,bw,'PERFECT WOMEN',7,'Helvetica-Bold',NAVY)
rr(c,M,14*mm,W-2*M,18*mm,3*mm,fill=YELLOW); ctr(c,M,20*mm,W-2*M,'SIMPLE FOOD • CLEAR PORTIONS • REAL LIFE',12,'Helvetica-Bold',NAVY); c.showPage()
# rules
bg(c,2); header(c); title(c,'THE TAMMY RULES','Simple food • clear portions • real life'); rules=[('1','WEIGH IT RIGHT','Chicken, mince, beef, fish and butternut are weighed RAW.'),('2','DRY / DRAINED','Pasta and oats are weighed DRY. Tuna is weighed DRAINED.'),('3','VEG IS FLEXIBLE','Low-calorie non-starchy vegetables and salad are unlimited.'),('4','ONE STARCH','ONE starch per meal. Never combine two starches in the same meal.'),('5','TWO TREATS','Maximum TWO planned treat occasions per week.'),('6','WATER','Aim for about 3 litres of water each day.')]; y=H-78*mm
for i,(n,h,b) in enumerate(rules):
 fill=PB if i%2==0 else PC; acc=TEAL if i%2==0 else CORAL; rr(c,M,y-28*mm,W-2*M,23*mm,4*mm,fill=fill,stroke=acc); c.setFillColor(acc); c.circle(M+9*mm,y-16*mm,5*mm,fill=1,stroke=0); ctr(c,M+4*mm,y-18.5*mm,10*mm,n,9,'Helvetica-Bold',WHITE); tx(c,M+20*mm,y-13*mm,h,9.3,'Helvetica-Bold',NAVY); wrap(c,b,M+20*mm,y-21*mm,W-2*M-25*mm,7.8); y-=32*mm
rr(c,M,15*mm,W-2*M,20*mm,4*mm,fill=YELLOW); ctr(c,M,23*mm,W-2*M,'SAME FOODS • SAME HABITS • SIMPLE CONSISTENCY',10,'Helvetica-Bold',NAVY); c.showPage()
# portions
bg(c,3); header(c); title(c,'PORTION GUIDE','Use these as practical starting portions'); rows=[('Chicken breast','150 g','raw'),('Lean mince','150 g','raw'),('Lean beef','150 g','raw'),('Fish','150-180 g','raw'),('Tuna','110-130 g','drained'),('Eggs','2 large','counted'),('Cottage cheese','60-80 g','as served'),('Wholewheat pasta','60-75 g','dry'),('Oats','40-50 g','dry'),('Butternut','150-200 g','raw'),('Wholewheat wrap','1 medium','counted'),('Banana','1 medium','counted'),('Low-cal mayo','1 tbsp / 15 ml','measured'),('Honey','1 tsp / 5-7 g','measured'),('Low-fat milk','200-250 ml','measured')]; x=M; y=H-78*mm; cw=[72*mm,45*mm,55*mm]
for h,wc in zip(['FOOD','PORTION','HOW TO WEIGH'],cw): rr(c,x,y,wc,10*mm,0,fill=TEAL); ctr(c,x,y+3*mm,wc,h,7.3,'Helvetica-Bold',WHITE); x+=wc
y-=10*mm
for i,row in enumerate(rows):
 x=M; fill=PB if i%2==0 else WHITE
 for cell,wc in zip(row,cw): rr(c,x,y,wc,10*mm,0,fill=fill,stroke=LIGHT,lw=.6); tx(c,x+2.5*mm,y+3*mm,cell,7.1,'Helvetica',INK); x+=wc
 y-=10*mm
rr(c,M,15*mm,W-2*M,29*mm,4*mm,fill=PY,stroke=YELLOW); tx(c,M+5*mm,33*mm,'UNLIMITED VEG',9,'Helvetica-Bold',NAVY); wrap(c,'Lettuce, spinach, tomato, cucumber, peppers, broccoli, cauliflower, cabbage, green beans, courgettes, mushrooms, onions and similar low-calorie non-starchy vegetables.',M+5*mm,25*mm,W-2*M-10*mm,7.4,max_lines=3); c.showPage()
# breakfast snacks
bg(c,4); header(c); title(c,'BREAKFAST & SNACKS','Keep it repeatable'); bw=(W-2*M-5*mm)/2; card(c,M,H-119*mm,bw,52*mm,'BREAKFAST OPTIONS','High-protein Futurelife with fat-free milk. Oats 40-50 g dry + 1 tsp honey on higher-training days. 2 scrambled eggs. Futurelife / All-Bran with fat-free milk.',PB,TEAL); card(c,M+bw+5*mm,H-119*mm,bw,52*mm,'MORNING SNACK','Use only if hungry or the day is long. 1 medium banana OR 2 large eggs.',PC,CORAL); rr(c,M,H-194*mm,W-2*M,60*mm,4*mm,fill=WHITE,stroke=LIGHT); tx(c,M+5*mm,H-149*mm,'AFTERNOON OPTIONS',10,'Helvetica-Bold',NAVY); yy=H-162*mm
for o in ['2 large eggs','First Choice protein shake','2 crackerbread + 60-80 g fat-free cottage cheese','1 medium banana if you are running later']: bullet(c,M+7*mm,yy,o,CORAL,W-2*M-14*mm); yy-=11*mm
rr(c,M,18*mm,W-2*M,34*mm,4*mm,fill=PY,stroke=YELLOW); ctr(c,M,39*mm,W-2*M,'SNACKS ARE OPTIONAL.',10,'Helvetica-Bold',NAVY); ctr(c,M,29*mm,W-2*M,'Do not add food just because the plan has a snack slot.',8,'Helvetica',INK); c.showPage()
# lunch
bg(c,5); header(c); title(c,'LUNCH','Protein + vegetables + ONE starch'); lunches=[('PASTA + MINCE','150 g lean mince raw + 60-75 g wholewheat pasta dry + unlimited veg.'),('PASTA + TUNA','110-130 g tuna drained + 60-75 g wholewheat pasta dry + 1 tbsp low-cal mayo.'),('CHICKEN + BUTTERNUT','150 g chicken raw + 150-200 g butternut raw + unlimited veg.'),('WRAP','1 medium wholewheat wrap + chicken / tuna / mince + 60-80 g cottage cheese + salad.'),('GREEN SALAD','Large green salad + a full protein portion. Add ONE starch only if needed.')]; y=H-79*mm
for i,(h,b) in enumerate(lunches): fill=PB if i%2==0 else PC; acc=TEAL if i%2==0 else CORAL; rr(c,M,y-34*mm,W-2*M,29*mm,4*mm,fill=fill,stroke=acc); tx(c,M+5*mm,y-14*mm,h,9.3,'Helvetica-Bold',NAVY); wrap(c,b,M+5*mm,y-23*mm,W-2*M-10*mm,8,max_lines=3); y-=38*mm
rr(c,M,16*mm,W-2*M,24*mm,4*mm,fill=YELLOW); ctr(c,M,26*mm,W-2*M,'PASTA OR BUTTERNUT OR WRAP — NEVER TWO.',10,'Helvetica-Bold',NAVY); c.showPage()
# dinner
bg(c,6); header(c); title(c,'DINNER','Keep the formula simple'); gap=5*mm; bw=(W-2*M-2*gap)/3
for i,(head,body,fill,acc) in enumerate([('PROTEIN','150 g chicken / lean beef / lean mince raw, or 150-180 g fish raw.',PC,CORAL),('VEGETABLES','Unlimited non-starchy vegetables or a large salad.',PB,TEAL),('ONE STARCH','Use butternut or another planned starch when needed. One only.',PY,YELLOW)]): x=M+i*(bw+gap); card(c,x,H-127*mm,bw,54*mm,head,body,fill,acc)
rr(c,M,H-206*mm,W-2*M,62*mm,4*mm,fill=WHITE,stroke=LIGHT); tx(c,M+5*mm,H-158*mm,'EASY DINNER IDEAS',10,'Helvetica-Bold',NAVY); yy=H-171*mm
for o in ['Fish + large salad','Chicken + vegetables','Beef stew + vegetables','Lean mince + vegetables','Protein + vegetables + butternut on a hard training day']: bullet(c,M+7*mm,yy,o,TEAL,W-2*M-14*mm); yy-=9.5*mm
rr(c,M,16*mm,W-2*M,25*mm,4*mm,fill=PY,stroke=YELLOW); ctr(c,M,27*mm,W-2*M,'MORE TRAINING CAN CHANGE WHICH STARCH YOU USE.',9.2,'Helvetica-Bold',NAVY); ctr(c,M,21*mm,W-2*M,'It does not create permission for a second starch.',7.4,'Helvetica',INK); c.showPage()
# training swaps
bg(c,7); header(c); title(c,'TRAINING DAYS & SWAPS','Use the rule, not guesswork'); bw=(W-2*M-5*mm)/2; card(c,M,H-122*mm,bw,55*mm,'HIGHER-TRAINING DAY','Breakfast: oats + honey can work well. Late run: a banana beforehand can be useful. Dinner: butternut can be your ONE starch. Do not stack another starch on top.',PB,TEAL); card(c,M+bw+5*mm,H-122*mm,bw,55*mm,'EASIER / REST DAY','Choose a simpler breakfast. Use salad or vegetables freely. Keep the same protein portions. You may not need a starch at every meal.',PC,CORAL); rr(c,M,H-213*mm,W-2*M,72*mm,4*mm,fill=WHITE,stroke=LIGHT); tx(c,M+5*mm,H-155*mm,'ONE-STARCH SWAP EXAMPLES',10,'Helvetica-Bold',NAVY); swaps=['60-75 g dry pasta  ↔  150-200 g raw butternut','1 medium wholewheat wrap  ↔  150-200 g raw butternut','Burger bun  ↔  potato / butternut — choose the bun OR the side','Sunday lunch: one measured starch, not a plate of every starch']; yy=H-170*mm
for i,s in enumerate(swaps): rr(c,M+6*mm,yy-5*mm,W-2*M-12*mm,10*mm,3*mm,fill=PB if i%2==0 else PC); ctr(c,M+6*mm,yy-1.8*mm,W-2*M-12*mm,s,7.4,'Helvetica-Bold',NAVY); yy-=14*mm
c.showPage()
# weekends
bg(c,8); header(c); title(c,'WEEKENDS & TREATS','Enjoy them without losing the week'); card(c,M,H-124*mm,bw,58*mm,'SUNDAY LUNCH','Keep the same protein portion. Fill the plate with vegetables / salad. Choose ONE starch. Skip the second helping just because it is Sunday.',PY,YELLOW); card(c,M+bw+5*mm,H-124*mm,bw,58*mm,'TREAT RULE','Maximum two treat OCCASIONS per week. Plan them. Enjoy them. Return to normal at the next meal.',PC,CORAL); rr(c,M,H-222*mm,W-2*M,80*mm,4*mm,fill=WHITE,stroke=LIGHT); tx(c,M+5*mm,H-155*mm,'FAKEAWAY IDEAS',10,'Helvetica-Bold',NAVY); yy=H-169*mm
for h,b in [('CHICKEN WRAP','1 wrap + 150 g chicken + salad + cottage cheese.'),('BURGER','Lean patty + bun + salad. No chips or extra starch.'),('PASTA BOWL','150 g lean mince + 60-75 g dry wholewheat pasta + veg.'),('FISH PLATE','150-180 g fish + salad + one planned starch if wanted.')]: tx(c,M+6*mm,yy,h,8.4,'Helvetica-Bold',CORAL); wrap(c,b,M+42*mm,yy,W-2*M-48*mm,7.7,max_lines=2); yy-=13*mm
rr(c,M,15*mm,W-2*M,23*mm,4*mm,fill=PB,stroke=TEAL); ctr(c,M,26*mm,W-2*M,'SKINNY HOT CHOCOLATE = SKINNY / NO-ADDED-SUGAR POWDER.',8.4,'Helvetica-Bold',NAVY); ctr(c,M,20*mm,W-2*M,'Examples: NOMU Skinny Hot Chocolate or Lifestyle Food Skinny Hot Choc.',7.1,'Helvetica',INK); c.showPage()
# prep
bg(c,9); header(c); title(c,'MEAL PREP','Pick the method you will actually use'); preps=[('FULL BATCH • ~90 MIN','Weigh raw portions before cooking. Example: 900 g raw chicken = 6 x 150 g portions. Cook 2 proteins, roast 3-4 butternut portions, boil eggs, wash veg. Freeze later-week cooked protein.'),('SPLIT PREP • 45-60 MIN TWICE','Sunday for Mon-Wed, then Wed/Thu for the rest. Prep 3 x 150 g raw protein portions, 2-3 measured starch portions, boiled eggs and washed veg.'),('MIX & MATCH','Prepare components, not full meals: proteins, measured starch options and unlimited vegetables. Good for families.'),('MINIMAL PREP','Divide raw meats into 150 g portions and fish into 150-180 g portions. Keep tuna, wraps, crackerbread, cottage cheese, bananas, shakes, bagged salad and frozen veg ready.')]; y=H-80*mm
for i,(h,b) in enumerate(preps): fill=[PB,PC,PY,WHITE][i]; acc=[TEAL,CORAL,YELLOW,TEAL][i]; rr(c,M,y-44*mm,W-2*M,39*mm,4*mm,fill=fill,stroke=acc); tx(c,M+5*mm,y-14*mm,h,9,'Helvetica-Bold',NAVY); wrap(c,b,M+5*mm,y-23*mm,W-2*M-10*mm,7.4,max_lines=4); y-=47*mm
rr(c,M,15*mm,W-2*M,22*mm,4*mm,fill=YELLOW); ctr(c,M,23*mm,W-2*M,'600 g = 4 × 150 g • 750 g = 5 × 150 g • 900 g = 6 × 150 g',8.1,'Helvetica-Bold',NAVY); c.showPage()
# shopping
bg(c,10); header(c); title(c,'7-DAY SHOPPING LIST','For one person — adjust for your week'); cols=[('PROTEIN',['Chicken breasts','Lean mince / beef','Fish','Tuna','Eggs','Cottage cheese','Protein shakes']),('STARCH',['Wholewheat pasta','Oats / cereal','Butternut','Wholewheat wraps','Bananas','Crackerbread']),('VEG + EXTRAS',['Salad leaves','Tomatoes','Cucumber','Peppers','Broccoli / cauliflower','Low-cal mayo','Honey','Low-fat milk'])]; gap=5*mm; bw=(W-2*M-2*gap)/3
for i,(head,items) in enumerate(cols):
 x=M+i*(bw+gap); fill=[PB,PY,PC][i]; acc=[TEAL,YELLOW,CORAL][i]; rr(c,x,H-206*mm,bw,135*mm,4*mm,fill=fill,stroke=acc); ctr(c,x,H-86*mm,bw,head,9.5,'Helvetica-Bold',NAVY); yy=H-101*mm
 for item in items: c.setFillColor(TEAL if acc==YELLOW else acc); c.circle(x+6*mm,yy+1*mm,1.2*mm,fill=1,stroke=0); tx(c,x+11*mm,yy-1*mm,item,7.6,'Helvetica',INK); yy-=12*mm
rr(c,M,17*mm,W-2*M,34*mm,4*mm,fill=YELLOW); ctr(c,M,38*mm,W-2*M,'THE DAILY FORMULA',10,'Helvetica-Bold',NAVY); ctr(c,M,28*mm,W-2*M,'Protein first • unlimited veg • ONE starch • 3 L water • repeat',9,'Helvetica-Bold',NAVY); c.showPage(); c.save(); print(OUT)
