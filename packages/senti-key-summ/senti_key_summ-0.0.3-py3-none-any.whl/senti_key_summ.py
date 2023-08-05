
# finally summarization,kerwords and sentiment 
# !pip install requests bs4 transformers googletrans==3.1.0a0 gensim==3.6.0 textblob gradio sentencepiece
def data_summarizer():
    try:
        import requests
        from bs4 import  BeautifulSoup
        from googletrans import Translator
        import warnings
        warnings.filterwarnings("ignore")
        url = input("enter article url of Telugu/Hindi/English :")
        req = requests.get(url)
        # print(req)
        input_eng = ""
        soup = BeautifulSoup(req.text,"html.parser")
        for i in soup.findAll("p"):
            input_eng+=i.text.strip()
        # print(data)
        input_eng = input_eng[:2000]
        from transformers import pipeline
        sentiment = pipeline("sentiment-analysis",model = "distilbert-base-uncased-finetuned-sst-2-english")
        from transformers import PegasusForConditionalGeneration, AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        warnings.filterwarnings("ignore")
        # from gensim.summarization.summarizer import summarize
        from gensim.summarization import keywords
        from textblob import TextBlob
        translator = Translator()
        # from transformers import pipeline
        # summarizer = pipeline("summarization")
        from transformers import PegasusForConditionalGeneration, PegasusTokenizer
        from transformers import PegasusForConditionalGeneration, AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
        # tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
        translation=translator.translate(input_eng, dest = "en")
        tokens = tokenizer(translation.text, truncation=True, padding="longest", return_tensors="pt")
        # Summarize 
        summary = model.generate(**tokens)
        # Decode summary
        text = tokenizer.decode(summary[0]).replace("<pad> ","").replace("</s>","")
        # summary = summarizer(translation.text)
        # print(summary[0]['summary_text'])
        translator = Translator()
        # text = summary[0]['summary_text']
        # print(keywords(text,words = 5,lemmatize=False))
        key = keywords(text,words = 5,lemmatize=False)
        # print(key)
        translator = Translator()
        keys = translator.translate(key, dest = translator.detect(input_eng).lang)
        # print("keywords".center(50,"-"))
        # print(keys.text,end = " ")
        translator = Translator()
        out = translator.translate(text, dest = translator.detect(input_eng).lang)
        # senti = sentiment(text)[0]['label']
        analysis=TextBlob(text)
        #print(analysis.polarity)
        # print(analysis.sentiment)
        # print(f"Sentiment: {'Positive' if analysis.polarity > 0 else 'Negative' if analysis.polarity < 0 else 'Neutral' }")
        # return {"Output_summary :":out.text,"Keywords":keys.text.replace("\n",","),"Sentiment":f"{'Positive' if analysis.polarity > 0 else 'Negative' if analysis.polarity < 0 else 'Neutral' }"}
        # print(translation.text)
        # print(translation.extra_data)
        # return sentiment(out.text.strip())[0]['label'], keys.text.replace("\n",","), out.text.strip() 
        return {"Sentiment":sentiment(out.text.strip())[0]['label'],"Keywords":keys.text.replace("\n",","),"Summary":out.text.strip()}

    except Exception as e:
      raise e 


# input_eng = input()
# data_summarizer()
# import gradio as gr   
# interface = gr.Interface(fn=data_summarizer, 
#                          inputs=gr.inputs.Textbox(lines=20, placeholder='Past your  input text...'),outputs=['text',"text","text"])
# interface.launch(share = True, debug = False)
