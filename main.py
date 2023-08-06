import kivy
kivy.require('2.1.0')
import time
from datetime import date
from datetime import timedelta
import calendar
import plyer
import numpy as np
from plyer import notification
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
import webbrowser
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.utils import platform
from kivy.lang import Builder
from kivymd.app import MDApp
from dateutil.relativedelta import relativedelta


class IntroScreen(Screen):
    global new
    new = 1
    global url
    url= 'https://farhatblogs.blogspot.com/p/technical-support-for-legal-calculator.html'

    def openweb(self):  # for open menu web bage

        webbrowser.open(url,new=new)


class MainScreen(Screen):

    def up_grad(self):
        self.ids.btn5.text = get_display(arabic_reshaper.reshape('تحت التطوير'))

    def up_grad4(self):
        self.ids.btn6.text = get_display(arabic_reshaper.reshape('تحت التطوير'))

    def up_grad5(self):
        self.ids.btn7.text = get_display(arabic_reshaper.reshape('تحت التطوير'))


class CalcScreen(Screen):
    year = ObjectProperty(None)
    mon = ObjectProperty(None)
    day = ObjectProperty(None)
    global k
    def unupgrad(self):# for dtop app work if not update
       if date.today()==(2023,1,10):
           self.ids.slider.max== 2000
       else:
           self.ids.slider.max == 2050

    def upgrad(self):
        global ref
        ref = 0
        te = get_display(arabic_reshaper.reshape('أطلب النسخة النهائية لتفعيل الزر'))
        re = get_display(arabic_reshaper.reshape(''))
        re2 = get_display(arabic_reshaper.reshape(''))

        self.ids.result.text = te
        self.ids.result1.text = re
        self.ids.result2.text = re2

    def mins(self):
        day_e=0
        return day_

    def yr(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        year = today.year
        y = self.ids.year.text
        y = str(year)
        return y

    def mn(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        mon = today.month
        m = self.ids.mon.text
        m = str(mon)
        mom = str(mon)
        return m

    def dy(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        day = today.day
        m = self.ids.day.text
        d = str(day)
        return d

    def Up_datelable( self,first_value,second_value,Set=0,increment= "days"):
        try:



            year = self.year.text
            year = int(year)

            mon = self.mon.text
            mon = int(mon)

            day = self.day.text
            day = int(day) + day_e -day_e # this code for not excute except at all
            h = calendar.weekday(year, mon, day)
            print(h)
            if h == 4:

                self.ids.result.text = get_display(arabic_reshaper.reshape("أجازة إسبوعية"))
                self.ids.result1.text = get_display(arabic_reshaper.reshape("يوم جمعه"))
                self.ids.result2.text = get_display(arabic_reshaper.reshape("لا يحتمل صدور أى أحكام أو قرارات فيه"))
            else:
                day = int(day) + day_e
                if mon in [1, 3, 5, 7, 8, 10, 12] and day > 31:
                    day -= 31
                    mon += 1
                    if mon > 12:
                        mon -= 12
                        year += 1
                elif mon in [4, 6, 9, 11] and day > 30:
                    day -= 30
                    mon += 1
                elif mon == 2 and day >= 30 and year % 4 == 0:
                    day -= 29
                    mon = 3
                elif mon == 2 and day >= 29 and year % 4 != 0:
                    day -= 28
                    mon = 3
                # My_function2()
                p = time_add( first_value, second_value, day, mon, year,Set,increment)
                d = time_add.Fun(p)  # call function in class add time
                te = get_display(arabic_reshaper.reshape(str(do)))
                self.ids.result.text = te
                w = get_display(arabic_reshaper.reshape(str(re)))
                M = get_display(arabic_reshaper.reshape(str(re2)))
                if '!' in re:
                    self.ids.result1.text = w
                    self.ids.result1.color = 1, 0, 0, 1
                    self.ids.result1.text = w
                elif 'day' in re:
                    self.ids.result1.text = w
                    self.ids.result1.color = 0, 0, 1, 1
                    self.ids.result1.text = w
                else:
                    self.ids.result1.text = w
                    self.ids.result1.color = 0, 0, 0, 1
                    self.ids.result1.text = w
                self.ids.result.text = te
                self.ids.result2.text = M
        except:
            year = self.year.text
            year = int(year)
            mon = self.mon.text
            mon = int(mon)
            day = self.day.text
            day = int(day)
            h = calendar.weekday(year, mon, day)
            if h == 4:
                self.ids.result.text = get_display(arabic_reshaper.reshape("أجازة إسبوعية"))
                self.ids.result1.text = get_display(arabic_reshaper.reshape("يوم جمعه"))
                self.ids.result2.text = get_display(arabic_reshaper.reshape("لا يحتمل صدور أى أحكام أو قرارات فيه"))
            else:

                # My_function2()
                p = time_add( first_value, second_value, day, mon, year,Set,increment)
                d = time_add.Fun(p)  # call function in class add time
                te = get_display(arabic_reshaper.reshape(str(do)))
                self.ids.result.text = te
                w = get_display(arabic_reshaper.reshape(str(re)))
                M = get_display(arabic_reshaper.reshape(str(re2)))
                if '!' in re:
                    self.ids.result1.text = w
                    self.ids.result1.color = 1, 0, 0, 1
                    self.ids.result1.text = w
                elif 'day' in re:
                    self.ids.result1.text = w
                    self.ids.result1.color = 0, 0, 1, 1
                    self.ids.result1.text = w
                else:
                    self.ids.result1.text = w
                    self.ids.result1.color = 0, 0, 0, 1
                    self.ids.result1.text = w
                    self.ids.result.text = te
                    self.ids.result2.text = M


    def Up_datelable1(self,first_value, second_value,Set=0,increment="days"):

            year = self.year.text
            year = int(year)
            mon = self.mon.text
            mon = int(mon)
            day = self.day.text
            day = int(day)
            h = calendar.weekday(year, mon, day)
            if h == 4:
                self.ids.result.text = get_display(arabic_reshaper.reshape("أجازة إسبوعية"))
                self.ids.result1.text = get_display(arabic_reshaper.reshape("يوم جمعه"))
                self.ids.result2.text = get_display(arabic_reshaper.reshape("لا يحتمل صدور أى أحكام أو قرارات فيه"))
            else:

                # My_function2()
                p = time_add( first_value, second_value, day, mon, year,Set,increment,)
                d = time_add.Fun(p)  # call function in class add time
                te = get_display(arabic_reshaper.reshape(str(do)))
                self.ids.result.text = te
                w = get_display(arabic_reshaper.reshape(str(re)))
                M = get_display(arabic_reshaper.reshape(str(re2)))
                if '!' in re:
                    self.ids.result1.text = w
                    self.ids.result1.color = 1, 0, 0, 1
                    self.ids.result1.text = w
                elif 'day' in re:
                    self.ids.result1.text = w
                    self.ids.result1.color = 0, 0, 1, 1
                    self.ids.result1.text = w
                else:
                    self.ids.result1.text = w
                    self.ids.result1.color = 0, 0, 0, 1
                    self.ids.result1.text = w
                self.ids.result.text = te
                self.ids.result2.text = M


    def cancel_all(self):
        self.ids.result.text = get_display(arabic_reshaper.reshape(""))
        self.ids.result1.text = get_display(arabic_reshaper.reshape(""))
        self.ids.result2.text = get_display(arabic_reshaper.reshape(""))

    def upgrad_notif(self):
        self.ids.result.text = get_display(arabic_reshaper.reshape('إشترى نسختك لتفعيل التبييهات'))
        self.ids.result1.text = get_display(arabic_reshaper.reshape('للإتصال'))
        self.ids.result2.text = get_display(arabic_reshaper.reshape('للتواصل صفحه farhatblogs على الفيس بوك'  ))

    def yr(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        year = today.year
        y = self.ids.year.text
        y = str(year)
        return y

    def mn(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        mon = today.month
        m = self.ids.mon.text
        m = str(mon)

        return m

    def dy(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        day = today.day
        d = self.ids.day.text
        d = str(day)
        return d

    def notif(self):
        while True:
            import plyer
            from plyer import notification
            with open('calandar.txt', 'r') as clan:
                l = list()
                for line in clan.readlines():
                    date = line.rstrip()

                    info, date = date.split("--")

                    message = 'أخر ميعاد{}: {}'
                    message = message.format(info, date)

                    notification.notify(title='تذكير بميعاد', message=message, app_name='Legal calculator', app_icon="",
                                        timeout=10, ticker='ticker', toast=True)

            time.sleep(60 * 60 * 1)

class SettingsScreen(Screen):

    def view(self):

        with open('calandar.txt', 'r') as clan:
            l = list()
            count = 0
            for line in clan.readlines():
                date = line.rstrip()
                try:
                    info, time, itr = date.split("--")
                except:
                    info, time = date.split("--")
                    global h
                h = 'الميعاد' + ' ' + info + 'البيان' + '  ' + time + '\n'
                count += 1
                l.append(h)
                self.ids.lists.text = self.ids.lists.text + get_display(arabic_reshaper.reshape(h))
                continue
                if count == len(l):
                    break

    def dell_all(self):
        File = "calandar.txt"
        with open(File, 'r') as filedata:
            Filelines = filedata.readlines()
            # storing the current line number in a variable
            lineindex = 1
            deleteLine = 1

            with open(File, 'w') as filedata:
                for textline in Filelines:
                    if lineindex != deleteLine:
                        filedata.write(textline)
                        lineindex += 1

    def refresh(self):
        self.ids.lists.text = ''

    def del_date(self):

        with open('calandar.txt', 'r') as clan:
            for line in clan.readlines():
                date = line.rstrip()
                clan.clear.date


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class EriaScreen(Screen):
    def spinner_clicked1(self, value):
        self.ids.My_city.text = value

    def spinner_clicked2(self, value):
        self.ids.My_cor.text = value

    def btn_eria(self):
        Y = None
        X = None
        global day_e
        day_e = 0
        My_arr = np.array([[Alexandria, Aswan, Asyut, Banha, Bani_Sweif, Cairo, Damanhur, Damietta, Fayoum, Mansoura,
                            Minya, Hurghada, Matrouh, Edfu, Ismailia, Kafr_El_Sheikh, Luxor, Mahalla, Malawi, Port_Said,
                            Qena, shrmalshykh,Shbeen_El_Koom, Sohag, Suez, Tanta, Zagazig]], dtype=object)
        t = self.ids.spinner1.text
        u = self.ids.spinner2.text
        for c in my_list:
            if c == t:
                # print(c)
                Y = my_list.index(c)

                print(Y)
                break

        for c in my_list:
            # print(c)
            if c == u and day_e != 60:
                # print(c)
                X = my_list.index(c)
                # print(My_arr.ndim)
                # print (X)
                result = (My_arr[0, Y])[X]
                print(result)

                o = result // 50
                if o <= 0 or result == 50:  ## can for out in egypt  befor(or)  add --and result \50 !=.02  ====day_e=30 and do thing for mon_e
                    day_e = day_e
                elif result > 50 and o == 1:
                    day_e += 1
                    if result - (o * 50) > 30:
                        day_e += 1
                elif o == 2:
                    day_e += 2
                    if result - (o * 50) > 30:
                        day_e += 1
                elif o == 3:
                    day_e += 3
                    if result - (o * 50) > 30:
                        day_e += 1

                else:
                    day_e += 4
                print(day_e)
                print(result / 50)
                print()
                return day_e


class SaveScreen(Screen):

    def save(self):
        try:
            with open('calandar.txt', 'a') as clan:
                global k
                self.ids.lab.text = get_display(self.ids.lab.text)
                k = self.ids.input.text
                # itr = self.ids.day_not.text
                global l
                F = str(date_final).split("-")
                f = list(F)
                l = list()
                for x in f:
                    x = str(x)
                    l.append(x)
                f = (' ').join(l[:])
                clan.write(f + '--' + k + '--' + '\n')  # str(itr) + '\n')
                # notif()
        except:
               None

class AddScreen(Screen):
    def upgrad1(self):
        self.ids.btn1.text = get_display(arabic_reshaper.reshape('إشترى نسحه كامله لتفعيل الزر'))

    def upgrad2(self):
        self.ids.btn2.text = get_display(arabic_reshaper.reshape('إشترى نسحه كامله لتفعيل الزر'))

    def upgrad3(self):
        self.ids.btn3.text = get_display(arabic_reshaper.reshape('إشترى نسحه كامله لتفعيل الزر'))

class CutScreen(Screen):

    def yr(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        year = today.year
        global  y
        y = self.ids.year.text
        y = str(year)

        return y

    def mn(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        mon = today.month
        m = self.ids.mon.text
        m = str(mon)
        mom = str(mon)
        return m

    def dy(self):  # for update the text in lable
        today = date.today()  # to start calculated in real day today now
        day = today.day
        m = self.ids.day.text
        d = str(day)
        return d
    def slim_1(self):
       pass

class time_add :

    from datetime import date
    def __init__ (self ,first_value,second_value ,day,mon,year,Set,increment):# increment( days.months,years) first_value for days main second for monthe or my be years if
        self.Set= Set
        self.increment=increment
        self.first_value= first_value
        self.second_value = second_value
        self.day = day
        self.mon = mon
        self.year = year
    def Fun (self):
       global date_final
       date_final=date(self.year ,self. mon ,self .day )
       if self .increment== "days" and self.second_value ==0:
              date_final += relativedelta(days =(self.first_value))# months,years
       elif self .increment =="months"and  self.second_value ==0:
              date_final += relativedelta(months=(self.first_value))
              date_final -= relativedelta(days=(1))
       elif self .increment =="years"and  self.second_value ==0:
              date_final += relativedelta(years=(self.first_value))
              date_final-=relativedelta(days =(1))
       elif self.increment == "months" and self.second_value != 0:
              date_final += relativedelta(months=(self.first_value))
              date_final +=relativedelta(days =(self.second_value))
              date_final -= relativedelta(days=(1))
       week_day=date_final.weekday()
       #date_final +=self.value
       print(date_final)
       if week_day == 0:
          week_day = 'لإثنين'

       elif week_day == 1:
            week_day = 'الثلاثاء'

       elif week_day == 2:
            week_day = 'الأربعاء'
       elif week_day == 3:
            week_day = 'الخميس'
       elif week_day == 5:
            week_day = 'السبت'
       elif week_day == 6:
            week_day = 'الأحد'
       elif week_day == 4:
            week_day += 1
            week_day = 'مد للسبت'  # for fireday
            date_final += relativedelta(days=(1))
       global do
       do = "أخر ميعاد", week_day, str(date_final)
       today = date.today()
       g = date(self.year, self.mon, self.day)
       time = date_final - today
       Time = str(time)
       Time = Time.replace('days', 'يوم')
       global re
       global re2
       if '-' in str(time):
           # result_t('عذرا لقد فات الميعاد','غير متوقع')

           re = '!عذرا لقد فات الميعاد'
       elif 'يوم' not in Time:
           # result_t(Time,'إنتبه اليوم ينتهى الميعاد')

           re = Time, 'إنتبه اليوم ينتهى الميعاد'
       else:
           # result_t(Time,'باقى من الميعاد')

           re = 'باقى من الميعاد', Time


       if self.first_value == 1 and self.increment =="months":

           re2 = 'يحسب الوقف الجزائى من تاريخ الوقف 15 يوم من إنتهاء شهر الوقف مادة 99 مرافعات'

       elif self.first_value ==  6 and self.Set == 0 and self .increment=="months" :
           re2 = 'يحسب تجديد الوقف التعليقى 6 أشهر من تاريخ إنتهاء سبب الوقف مادة 134 مرافعات'

       elif self.first_value ==  6 and self.Set == 1 and self .increment=="months" :

           re2 = 'يحسب سقوط الخصومة ستة أشهر من تاريخ أخر إجراء صحيح ماده 134 مرافعات'
       elif self.first_value  == 2 and  self.Set == 0 and self .increment=="years":
           re2 = 'تنقضى الخصومة بإنقضاء سنتان من أخر إجراء صحيح فيهامادة 140 مرافعات'
       elif self.first_value ==6  and  self.Set == 2 and self .increment=="months" :

           re2 = 'يقدم طلب الإعفال قبل إنقضاء ستة أشهر من يوم نهايئة الحكم المغفل\n ماده 134 مرافعات'
       elif self.first_value == 60 and self.Set == 0:
           re2 = 'يحسب ميعاد النقض 60 يوم من تاريخ الحكم أو إعلانه  '
       elif  self.first_value == 40 and self.Set==0:
           re2 = 'يحسب ميعاد الإستئناف 40 يوم من تاريخ الحكم أو إعلانه ماده 227 مرافعات'
       elif self.first_value == 15  and self.Set==0:

           re2 = 'يحسب ميعاد إستئناف المستعجل 15 يوم من تاريخ الحكم أو إعلانه مادة 227 مرافعات'
       elif self.first_value == 10 and self.Set == 0 :
           re2 = 'يحسب ميعاد التظلم فى الأمر الصادر بالأداء 10 أيام مادة 206 مرافعات '
       elif self.first_value == 8 and self.Set == 0:
           re2 = 'يجب إعلان شواهد الطعن بالتزوير قبل إنقضاء 8 أيام من التقرير به'
       elif self.first_value == 60 and self.Set == 1:
           re2 = 'تجدد الدعوى من الشطب خلال 60 يوم من قرار الشطب مادة 82 مرافعات'
       elif self.first_value == 40 and self.Set == 1:
           re2 = 'يحسب ميعاد إعادة النظر 40 من يوم صدور الحكم المستأنف أو الإعلان به\n كأصل عام ماده 242 مرافعات'
       elif self.first_value == 8 and self.Set == 1:
           re2 = 'ميعاد الطعن فى تقدير الرسوم 8 أيام من تاريخ الإعلان بالتقدير ماده 190 مرافعات'
       elif self.first_value == 3 and self.Set == 0 and self .increment=="months":
           re2 = 'يسقط أمر الصادر على عريضه إذا لم يتم تنفيذه خلال ثلاث أشهر \nمن تاريخ صدوره ماده 200 مرافعات'
       elif self.first_value == 15 and self.Set == 1 :

           re2 = 'يحب ميعاد الطعن فى القرار الصادر من النيابة العامة بالحيازة 15 يوم\n من تاريخ صدوره أو إعلانه'
       elif self.first_value == 60 and  self.Set == 2:
           re2 = 'يحسب ميعاد الطعن على القرار الإدارى 60 يوم من تاريخ إعلانه أو نشره  '
       elif self.first_value == 60 and self.Set == 3:
           re2 = 'يحسب ميعاد الطعن على القرار الجزاء 60 يوم من تاريخ إعلانه   '
       elif self.first_value  == 3 and self.Set == 1 and self .increment=="months":
           re2 = 'يعتبرأمر الأداء كأن لم يكن إذا لم يعلن للمدين خلال 3 شهور ماده 205 مرافعات  '
       elif self.first_value == 8  and self.Set == 2:
           re2 = 'يعتبر الحجز التحفظى كأن لم يكن إذا لم يعلن محضر الحجز للمحجوز عليه\n خلال 8 أيام من بتوقيعه مادة 320 مرافعات'
       elif self.first_value == 8 and  self.Set == 3 :
           re2 = 'يجب أن ترفع دعوى صحة الحجز خلال 8 أيام من تاريخ الحجز بأمر قاضى التنفيذ\n مادة 333 مرافعات'
       elif self.first_value == 30 and self.Set == 0:
           re2 = 'يكون الإعتراض على إنذار الطاعه خلال  30 يوم من الإعلان بالدخول فى الطاعة'
       elif self.first_value == 3 and self.Set == 2  and  self.increment=="months":
           re2 = 'يسقط الحق فى الشكوى بمرور 3 شهور من تاريخ العلم بالجريمة و مرتكبها'
       elif self.first_value == 10  and self.Set == 1:
           re2 = 'يستأنف الحكم الصادر فى الجنحة خلال 10 أيام من تاريخ الحكم الحضورى'
       elif self.first_value == 3 and self.increment =="years":
           re2 = 'تتقادم الجنحة بمرور 3 سنوات من تاريخ وقوعها أو أخر إجراء صحيح فيها'
       elif self.first_value ==  10 and self.Set==2:
           re2 = 'تتقادم الجنايه بمرور 10 سنوات من تاريخ وقوعها أو أخر إجراء صحيح فيها'
       elif self.first_value ==  1  and self .increment== "years":
           re2 = 'تتقادم المخالفة بمرورسنه من تاريخ وقوعها أو أخر إجراء صحيح فيها'
       elif self.first_value == 4 and self .increment=="months":
           re2 = 'يجب إبداء الرغبة فى الأخذ بالشفعة خلال 4 شهور من تاريخ التسجيل مادة 948 مدنى'
       elif self.first_value == 90 and self.Set == 0:
           re2 = 'يجب إيداع قائمة شروط البيع خلال تسعين يوم من تسجيل التبيه بنزع الملكية\n ولا إعتبر كأن لم يكن ماده 414 مرافعات'


# ---- for add time_eria  refranice by http://iskandrany.6te.net/distances.htm
Alexandria = [0, 1133, 593, 167, 332, 216, 60, 221, 295, 175, 459, 761, 323, 1025, 260, 113, 662, 148, 506, 273, 847,
              716, 151, 699, 348, 123, 180]
Aswan = [1133, 0, 540, 975, 801, 926 ,1079, 1124, 852 ,1058, 674, 500, 1435, 112, 1066, 1066, 229, 1041, 627 ,1146 ,286
         ,1429, 988, 434, 1061, 1016, 1012]
Asyut = [593, 540, 0, 453, 261, 386, 539, 584, 312, 518, 134, 458, 895, 432, 526, 521, 322, 501, 87, 606, 254, 889, 448,
         106, 521, 476, 472]
Banha = [167, 975, 453, 0, 174, 49, 141, 149, 140, 83, 301, 597, 490, 867, 117, 89, 757, 69, 348, 181, 689, 552, 25,
         541, 184, 44, 37]  # for eril for law
Bani_Sweif = [332, 801 ,261, 174, 0, 125, 278, 323 ,51, 257, 127, 464, 634, 693 ,256, 260 ,583 ,240 ,174 ,345 ,515, 628,
              187, 367, 260 ,215, 211]
Cairo = [216, 926, 386, 49, 125, 0, 156, 198, 91, 132, 252, 548, 524, 524, 140, 138, 708, 118, 299, 220, 640, 503, 66,
         492, 135, 93, 86]
Damanhur = [60, 1079, 539, 141 ,278, 156, 0, 161 ,244 ,115 ,405 ,701, 383 ,971, 200, 53, 861, 88, 452, 213, 793, 656
            ,91 ,645 ,288, 63 ,154]
Damietta = [221, 1124, 584, 149, 323, 198, 161, 0, 286, 66, 450, 647, 544 ,1016, 146, 108, 906 ,89, 497, 66, 838 ,602
            ,142, 609 ,234, 114, 123]
Fayoum = [295, 852, 312, 140, 51, 91, 244, 286, 0, 237, 164, 501, 597, 730, 245, 240, 620, 220, 211, 325, 552, 608, 167,
          404, 240, 181, 177]
Mansoura = [175, 1058, 518, 83, 257, 132, 115, 66, 237, 0, 384, 630, 498, 950, 129, 66, 840, 27, 431, 98, 772, 585, 80,
            624, 217, 52, 57]
Minya = [459, 674, 134, 301, 127, 252, 405, 450, 164, 384 , 0 ,	452 ,	761 ,	566 ,	392 ,	387 ,	456 ,	367 ,	47  ,472, 388, 755, 314,
         240 ,387, 342, 338]
Hurghada = [761, 500, 458, 597, 464, 548, 701, 647 ,501, 630, 452, 0, 1072, 392, 501, 681, 282, 642, 499, 581, 214, 781
            ,614, 360, 413 ,638 ,581]
Matrouh = [323, 1435, 895, 490, 634, 524, 383, 544, 597, 498, 761, 1072, 0, 1327, 583, 436, 1217, 471, 808, 596, 1149,
           1227, 474, 1001, 659, 446, 503]
Edfu = [1025, 112, 432, 867, 693, 818, 971, 1016, 730, 950, 566, 392, 1327, 0, 958, 953, 121, 933, 519, 1038, 178, 1321,
        474, 1001, 659, 446, 503]
Ismailia = [260, 1066, 526, 117, 256, 140, 200, 146, 245, 129, 392, 501, 583, 958 ,  0 ,180, 848, 141, 439, 80, 780, 456,
            142, 632, 88, 137, 80]
Kafr_El_Sheikh = [113, 1061, 521, 89, 260 ,138, 53, 108, 240, 66 ,387, 681, 436, 953, 180, 0, 843, 39, 434, 164, 775,
                  636, 73, 627 ,268, 45, 102]
Luxor = [662, 229, 322, 757 ,583, 708, 861, 906, 620, 840, 456, 282, 1217, 121, 848, 843, 0, 823 ,409 ,928, 68, 1211,
         770, 216, 843, 798, 794]
Mahalla = [148, 1041, 501, 69, 240, 118, 88, 89, 220, 27, 367, 642, 471, 933, 141, 39, 823, 0, 414, 125, 755, 597, 53,
           607, 229, 25, 67]
Malawi = [506, 627 ,87, 348, 174, 299, 452, 497, 211, 431 ,47 ,499, 808, 519, 439 ,434, 409, 414, 0, 519, 341, 802, 361,
          87 ,434, 386, 385]
Port_Said = [273, 1146, 606, 181, 345, 220, 213, 66, 325, 98, 472, 581, 596, 1038, 80, 164, 928, 125, 519, 0, 860, 536,
             178, 712, 168, 150, 154]
Qena = [847, 286, 254, 689, 515, 640, 793, 838 ,552, 772, 388, 214, 1149, 178, 780, 775, 68, 755, 341, 860, 0, 1143
        ,702, 148, 775, 730, 726]
shrmalshykh = [716, 1429, 889, 552, 628, 503, 656, 602, 608, 585, 755, 781, 1227, 1321, 456, 636, 1211, 597, 802, 536,
               1143, 0, 569, 995, 368, 593, 536]
Shbeen_El_Koom = [151, 988, 448, 25, 187, 66, 91, 142, 167, 80, 314, 614, 474, 880, 142, 73, 770, 53, 361, 178, 702,
                  569, 0, 554, 201, 28, 62]
Sohag = [699, 434, 106, 541, 367, 492, 645, 690, 404, 624, 240, 360, 1001, 326, 632, 268, 216, 607, 87, 712, 148, 995,
         554, 0, 627, 582, 578]
Suez = [348, 1061, 521, 184, 260, 135, 288, 234, 240, 217, 387, 413, 659, 953, 88, 627, 843, 229, 434, 168, 775, 368,
        201, 627, 0, 225, 168]
Tanta = [123, 1016, 476, 44, 215, 93, 63, 114, 181, 52, 342, 638, 446, 908, 137, 45 ,798, 25, 386, 150 ,730, 593, 28,
         582, 225, 0, 57]
Zagazig = [180, 1012, 472, 37, 211, 86, 154, 123, 177, 57, 338, 581, 503, 904, 80, 102, 794, 67, 385, 154, 726, 536, 62,
           578, 168, 57, 0]
my_list = ['Alexandria', 'Aswan ', 'Asyut', 'Banha', 'Bani_Sweif', 'Cairo', 'Damanhur', 'Damietta ', 'Fayoum',
           'Mansoura', 'Minya', 'Hurghada', 'Matrouh', 'Edfu', 'Ismailia ', 'Kafr_El_Sheikh', 'Luxor', 'Mahalla',
           'Malawi', 'Port_Said', 'Qena','shrmalshykh', 'Shbeen_El_Koom', 'Sohag', 'Suez', 'Tanta', 'Zagazig', ]  # 'out_of_Egypt']


class MyApp(App):

    def build(self):
        self.icon="icon.jpg"
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name='intro'))
        sm.add_widget(CalcScreen(name='calc'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(EriaScreen(name='eria'))
        sm.add_widget(AddScreen(name='add'))
        sm.add_widget(SaveScreen(name='save'))
        sm.add_widget(CutScreen(name='cut'))

        sm.current = 'intro'
        return sm

if __name__ == '__main__':
    MyApp().run()

