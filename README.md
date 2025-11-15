# customer-outreach-ai-agent
---

### **Agentlar**

* **sales_rep_agent (Savdo vakili)**

  * Maqsad: Ideal mijoz profiliga mos keladigan yuqori qiymatli leadlarni aniqlash.
  * Vazifa: Raqamli makonni kuzatib, ma’lumot va trendlarni tahlil qilish orqali yangi imkoniyatlarni topish.

* **lead_sales_rep_agent (Yetakchi savdo vakili)**

  * Maqsad: Leadlarni shaxsiylashtirilgan va ta’sirli muloqotlar orqali rivojlantirish.
  * Vazifa: Leadlar bilan personalizatsiyalangan xabarlar orqali bog‘lanib, ularni sodiq mijozga aylantirish.

---

### **Tasklar**

* **lead_profiling_task**

  * Lead kompaniyasini chuqur tahlil qilish, asosiy qaror qabul qiluvchilar va ehtiyojlarni aniqlash.
* **personalized_outreach_task**

  * Lead profiling hisobotiga asoslanib, shaxsiylashtirilgan outreach kampaniyasi yaratish.
  * SentimentAnalysisTool yordamida ijobiy va jozibali xabarlar tayyorlash.

---

### **Crew**

* Crew — bu agentlar va tasklarni birlashtiruvchi “orchestrator”.
* `crew.kickoff(inputs=inputs)` orqali berilgan lead ma’lumotlari asosida barcha tasklar ketma-ket bajariladi.
* `verbose=2` → jarayon haqida batafsil log beradi, `memory=True` → agentlar oldingi ma’lumotlarni yodda saqlaydi.

---

### **Inputs**

* Lead kompaniya va asosiy qaror qabul qiluvchi haqida ma’lumot:

  * Nomi: DeepLearningAI
  * Sanoat: Onlayn Ta’lim Platformasi
  * Qaror qabul qiluvchi: Endryu Ng, Bosh direktor
  * So‘nggi yutuq: mahsulotni ishga tushirish

---

### **Natija**

* `result` → AI agentlar yaratgan **batafsil hisobot va shaxsiylashtirilgan outreach xabarlar**.
* IPython orqali `Markdown(result)` bilan chiroyli formatda chiqarish mumkin.

---
