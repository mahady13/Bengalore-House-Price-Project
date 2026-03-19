#  Bengaluru House Price Predictor

একটি মেশিন লার্নিং প্রজেক্ট যা বেঙ্গালুরুর বিভিন্ন লোকেশন, বিএইচকে (BHK) এবং স্কয়ার ফিটের ওপর ভিত্তি করে বাড়ির দাম প্রেডিক্ট করতে পারে। এটি **Streamlit** দিয়ে তৈরি করা হয়েছে।

##  ফিচারসমূহ
- **Interactive UI:** ড্রপডাউন থেকে লোকেশন সিলেক্ট করার সুবিধা।
- **Real-time Prediction:** ইনপুট দেওয়ার সাথে সাথে বাড়ির সম্ভাব্য দাম (Lakhs এ) দেখা যায়।
- **ML Pipeline:** লিনিয়ার রিগ্রেশন (Linear Regression) মডেল ব্যবহার করা হয়েছে।

##  টেক স্ট্যাক (Tech Stack)
- **Language:** Python
- **Libraries:** Pandas, Scikit-learn, NumPy
- **Framework:** Streamlit
- **Deployment:** Docker & GitHub Actions (CI/CD)

##  প্রোজেক্ট স্ট্রাকচার
├── app.py              # মেইন স্ট্রিমলিট অ্যাপ
├── pipe.pkl            # ট্রেইন করা মেশিন লার্নিং মডেল
├── clean_data.csv      # প্রসেস করা ডাটাসেট
├── requirements.txt    # প্রয়োজনীয় লাইব্রেরির লিস্ট
└── Dockerfile          # কন্টেইনারাইজেশন ফাইল

## 💻 কীভাবে রান করবেন (Local Run)
১. রিপোজিটরি ক্লোন করুন:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/bengaluru-house-price-prediction.git](https://github.com/YOUR_USERNAME/bengaluru-house-price-prediction.git)
