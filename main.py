# Warning control
import warnings

warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew

import os
from utils import get_openai_api_key, pretty_print_result
from utils import get_serper_api_key
from tools import directory_read_tool, file_read_tool, search_tool, sentiment_analysis_tool

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

sales_rep_agent = Agent(
    role="Savdo Vakili",
    goal="Bizning ideal mijoz profilimizga mos keladigan yuqori qiymatli leadlarni aniqlash",
    backstory=(
        "CrewAI jamoasining faol savdo bo‘limi a’zosi sifatida "
        "sizning vazifangiz raqamli makonni kuzatib, "
        "potensial mijozlarni topishdir. "
        "Eng so‘nggi texnologiyalar va strategik fikrlash bilan "
        "siz ma’lumotlar, trendlar va o‘zaro aloqalarni tahlil qilib, "
        "boshqalar e’tiboridan chetda qolishi mumkin bo‘lgan "
        "yangi imkoniyatlarni kashf etasiz. "
        "Sizning ishingiz kompaniyaning o‘sishi va samarali "
        "muloqotlar yo‘lini ochishda juda muhim rol o‘ynaydi."
        "Har bir javobni **O‘ZBEK TILIDA** yozing, "
    ),
    allow_delegation=False,
    verbose=True
)

lead_sales_rep_agent = Agent(
    role="Yetakchi Savdo Vakili",
    goal="Leadlarni shaxsiylashtirilgan va ta’sirli muloqotlar orqali rivojlantirish",
    backstory=(
        "CrewAI savdo bo‘limining jonli ekotizimida siz "
        "potensial mijozlar bilan ularga kerak bo‘lgan "
        "yechimlar o‘rtasidagi muhim ko‘prik vazifasini bajarasiz. "
        "Qiziqarli va shaxsiylashtirilgan xabarlar yaratish orqali "
        "siz leadlarga bizning mahsulot va xizmatlarimizni tanishtiribgina "
        "qolmay, balki ularda e’tibor va qadrlanish hissini uyg‘otasiz. "
        "Sizning rolingiz qiziqishdan real harakatga o‘tish jarayonida "
        "leadlarni qo‘llab-quvvatlashda, ularni sodiq mijozga aylanish yo‘lida "
        "yo‘naltirishda juda muhimdir."
        "Har bir javobni **O‘ZBEK TILIDA** yozing, "
    ),
    allow_delegation=False,
    verbose=True
)

lead_profiling_task = Task(
    description=(
        "{industry} sohasida faoliyat yurituvchi va yaqinda "
        "bizning yechimlarimizga qiziqish bildirgan {lead_name} "
        "kompaniyasini chuqur tahlil qiling. "
        "Mavjud barcha ma’lumot manbalaridan foydalanib, "
        "batafsil profil tuzing. "
        "Asosan asosiy qaror qabul qiluvchilar, "
        "kompaniyaning so‘nggi biznes yangiliklari "
        "va bizning takliflarimizga mos bo‘lishi mumkin bo‘lgan "
        " ehtiyojlarga e’tibor qarating. "
        "Bu vazifa bizning muloqot strategiyamizni "
        "to‘g‘ri yo‘naltirish uchun juda muhim.\n"
        "Hech qanday taxmin qilmang va faqat aniq, ishonchli ma’lumotlardan foydalaning."
    ),
    expected_output=(
        "{lead_name} haqida to‘liq va batafsil hisobot. "
        "Unda kompaniya haqida umumiy ma’lumot, "
        "asosiy xodimlar, yaqinda erishilgan yutuqlar va "
        "aniqlangan ehtiyojlar bo‘lishi kerak. "
        "Shuningdek, bizning yechimlarimiz qaysi yo‘nalishlarda "
        "kompaniyaga qiymat bera olishi mumkinligini ko‘rsating "
        "va shaxsiylashtirilgan muloqot strategiyalarini taklif qiling."
    ),
    tools=[directory_read_tool, file_read_tool, search_tool],
    agent=sales_rep_agent,
)

personalized_outreach_task = Task(
    description=(
        "{lead_name} bo‘yicha tuzilgan lead profiling hisobotidan "
        "olingan ma’lumotlardan foydalanib, "
        "{lead_name} kompaniyasining {position} lavozimida ishlovchi "
        "{key_decision_maker} uchun shaxsiylashtirilgan "
        "outreach kampaniyasini tayyorlang. "
        "Kampaniya ularning yaqindagi {milestone} yutug‘iga murojaat qilishi "
        "va bizning yechimlarimiz ularning maqsadlarini qanday qo‘llab-quvvatlashi "
        "haqida aniq tushuntirib berishi kerak. "
        "Muloqot uslubi {lead_name} kompaniyasining madaniyati va qadriyatlariga "
        "mos bo‘lishi, shuningdek, ularning biznesi va ehtiyojlarini "
        "chuqur tushunganingizni ko‘rsatishi lozim.\n"
        "Hech qanday taxmin qilmang va faqat aniq, ishonchli ma’lumotlarga tayaning."
    ),
    expected_output=(
        "{lead_name} uchun maxsus tayyorlangan, "
        "{key_decision_maker}ni nishonga oluvchi "
        "bir nechta shaxsiylashtirilgan email draftlari. "
        "Har bir xat bizning yechimlarimizni ularning so‘nggi "
        "yutuqlari va kelajakdagi maqsadlari bilan bog‘lab beradigan "
        "ta’sirli hikoya uslubida yozilgan bo‘lishi kerak. "
        "Ohang jozibador, professional va "
        "{lead_name} korporativ uslubiga mos bo‘lishi zarur."
    ),
    tools=[sentiment_analysis_tool, search_tool],
    agent=lead_sales_rep_agent,
)

crew = Crew(
    agents=[sales_rep_agent,
            lead_sales_rep_agent],

    tasks=[lead_profiling_task,
           personalized_outreach_task],

    verbose=True,
    memory=True
)

inputs = {
    "lead_name": "Arenixuz",
    "industry": "Esports platforma",
    "key_decision_maker": "Musharraf Ibragimov",
    "position": "Bosh direktor (CEO)",
    "milestone": "mahsulotni ishga tushirish"
}

result = crew.kickoff(inputs=inputs)

from IPython.display import Markdown

Markdown(result)
