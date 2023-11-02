presets_data = [
    {
      "name": "Playground Generate Showcase - Product Feature to Benefit",
      "max_tokens": 200,
      "temperature": 0.4,
      "stop_sequences": [],
      "prompt": """Turn the following product feature into a list of benefits. Group them into three types of benefits: Functional Benefits, Emotional Benefits, and Social Benefits.

Product Feature:
Our app automatically transcribes your meetings. It uses state-of-the-art speech-to-text technology that works even in noisy backgrounds. Once the transcription is done, our app creates its summary and automatically emails it to the meeting attendees.""",
      "expected_output": """Functional Benefits:
- Save time by not having to manually transcribe your meetings
- Increase accuracy by not having to rely on human transcribers
- Reduce costs by not having to hire human transcribers 

Emotional Benefits:
- Reduce stress by not having to worry about transcribing your meetings
- Increase confidence by knowing that your meetings are being transcribed accurately
- Boost productivity by not having to spend time on transcribing your meetings 

Social Benefits:
- Encourage collaboration by sharing the meeting summary with the meeting attendees
- Improve communication by making sure that the meeting summary is accurate
- Increase transparency by providing a record of the meeting for everyone to see.""",
      "doc_url": "https://dashboard.cohere.ai/playground/shared-preset?ref=Product-Feature-to-Benefit-kddeaq&{query}&__hstc=14363112.4c7496d8370c0fedd2ec614ad3b4b31f.1698408367010.1698737477922.1698739703142.15&__hssc=14363112.18.1698739703142&__hsfp=2413774647"
    },
    {
      "name": "Playground Generate Showcase - Product Pitch",
      "max_tokens": 200,
      "temperature": 0.5,
      "stop_sequences": [],
      "prompt": """Generate a pitch for the following product: An AI chess tutor

The pitch must include the following sections.
1. Problem
2. Solution
3. Features
4. Buyer Persona
5. Business Model

Problem:""",
      "expected_output": """Problem: Chess is a game of precision and strategy, but it can be difficult to improve your game without access to a trained coach or tutor. If you feel like you're stuck at a plateau and want to get better at chess, you deserve access to the best tools! 

Solution:
Introducing the world's first AI chess tutor! This app uses cutting-edge AI to provide you with the guidance and feedback you need to improve your game.

Features:

-Cutting-edge AI
-User-friendly interface
-Hundreds of exercises and puzzles
-Video tutorials from world-class coaches
-Chatbot for instant feedback

Buyer Persona:

People who are passionate about improving their chess game, especially:

-Beginners looking for a way to learn the basics
-Intermediate players who want to improve their game
-Advanced players looking for a way to hone their skills 

Business Model:

-Freemium""",
      "doc_url": "https://dashboard.cohere.ai/playground/shared-preset?ref=Product-Pitch-8n7dkb&{query}&__hstc=14363112.4c7496d8370c0fedd2ec614ad3b4b31f.1698408367010.1698737477922.1698739703142.15&__hssc=14363112.18.1698739703142&__hsfp=2413774647"
    },
    {
      "name": "Playground Generate Showcase - Business Model Canvas",
      "max_tokens": 200,
      "temperature": 0.2,
      "stop_sequences": [],
      "prompt": """Generate a Business Model Canvas consisting of the following nine building blocks.
1 - Customer Segments
2 - Value Propositions
3 - Channels
4 - Customer Relationships
5 - Revenue Streams
6 - Key Resources
7 - Key Activities
8 - Key Partners
9 - Cost Structure

Business Model Canvas
Product: Satellite broadband service

1 - Customer Segments:""",
      "expected_output": """Residential customers, Small and medium-sized businesses, Large enterprises, Government and military institutions.

2 - Value Propositions:
Reliable and consistent internet connectivity, even in remote or rural areas.
Fast internet speeds ranging from 5 Mbps to 1 Gbps.
Affordable prices with flexible pricing plans.
Customer-centric support and service.

3 - Channels:
Satellite broadband service can be accessed through a satellite dish and modem, which can be purchased or rented from the service provider.
Marketing and advertising channels include online, print, and television advertising, as well as word-of-mouth referrals.

4 - Customer Relationships:
Long-term relationships with customers, with a focus on customer service and support.
Regularly communicate with customers to understand their needs and provide updates on service improvements.

5 - Revenue Streams:
Revenue is generated through monthly subscriptions for the satellite broadband service, with optional add-ons such as increased data usage or faster""",
      "doc_url": "https://dashboard.cohere.ai/playground/shared-preset?ref=Business-Model-Canvas-55np7x&{query}&__hstc=14363112.4c7496d8370c0fedd2ec614ad3b4b31f.1698408367010.1698737477922.1698739703142.15&__hssc=14363112.18.1698739703142&__hsfp=2413774647"
    },
    {
      "name": "Playground Generate Showcase - Email Keyword Extraction",
      "max_tokens": 40,
      "temperature": 0.4,
      "stop_sequences": ["--"],
      "prompt": """Extract the product and return address from this email:

Dear Elliott,

Unfortunately, your item, Supreme The North Face Statue of Liberty Baltoro Jacket, was not accepted for verification.
We will be shipping this back to 171 John Street, Toronto ON, M5T 1X2.

Product:""",
      "expected_output": """Supreme The North Face Statue of Liberty Baltoro Jacket
Return Address: 171 John Street, Toronto ON, M5T 1X2 
""",
      "doc_url": "https://dashboard.cohere.ai/playground/shared-preset?ref=Email-Keyword-Extraction-5ghcwn&{query}&__hstc=14363112.4c7496d8370c0fedd2ec614ad3b4b31f.1698408367010.1698737477922.1698739703142.15&__hssc=14363112.18.1698739703142&__hsfp=2413774647"
    },
    {
      "name": "Playground Generate Showcase - Simplify Technical Concepts",
      "max_tokens": 158,
      "temperature": 0,
      "stop_sequences": ["--"],
      "prompt": """Simplify the following technical explanation.

The core idea of information theory is that the informational value of a communicated message depends on the degree to which the content of the message is surprising. If a highly likely event occurs, the message carries very little information. On the other hand, if a highly unlikely event occurs, the message is much more informative.""",
      "expected_output": """Information theory is based on the idea that the more surprising an event is, the more information it carries.""",
      "doc_url": "https://dashboard.cohere.ai/playground/shared-preset?ref=Simplify-Technical-Concepts-tcjifr&{query}&__hstc=14363112.4c7496d8370c0fedd2ec614ad3b4b31f.1698408367010.1698737477922.1698739703142.15&__hssc=14363112.18.1698739703142&__hsfp=2413774647"
    },
    {
      "name": "Playground Generate Showcase - Keywords To Email",
      "max_tokens": 150,
      "temperature": 0.2,
      "stop_sequences": ["--"],
      "prompt": """Write an email about the following:
- launch of new fitness watch series
- email or live chat for any questions.""",
      "expected_output": """Hello, 

We are excited to announce the launch of our new fitness watch series. We have been working hard to bring you the best watches possible and we are confident that you will love them.

If you have any questions about the new series, please don't hesitate to contact us via email or live chat. We will be more than happy to help.

Thank you,
[Your Name]""",
      "doc_url": "https://dashboard.cohere.ai/playground/shared-preset?ref=Keywords-to-Email-egyyi5&{query}&__hstc=14363112.4c7496d8370c0fedd2ec614ad3b4b31f.1698408367010.1698737477922.1698739703142.15&__hssc=14363112.18.1698739703142&__hsfp=2413774647"
    },
    {
      "name": "Playground Generate Showcase - Victorian Style Writing",
      "max_tokens": 420,
      "temperature": 0.7,
      "stop_sequences": [],
      "prompt": """Turn the following text into beautiful and wandering Victorian prose without changing the original meaning.

Original Text:
"He was average." 

Victorian prose: 
"He was, in the way of most men, possessed of a rudimentary intelligence, his countenance ordinary, his bearing mild, with some weakness about the shoulders, his hair the color of ash; he spoke of the weather."

Original Text:
"It's a good thing America got to the moon first." 

Victorian prose:
"It is a matter of singular wonder that America, being the chief seat of learning and the repository of all arts and sciences, made herself mistress of the heavens, and in so doing reached across the blackness of cosmos to touch the gleaming silver moon."

Original Text:
"I'm feeling ok" 
Victorian prose:""",
      "expected_output": "I am at peace, with the weight of the world removed from my shoulders, and with a clear mind, untroubled by the trivialities of life, I feel an untroubled joy, and an untroubled hope, for my future.",
      "doc_url": "https://dashboard.cohere.ai/playground/shared-preset?ref=Victorian-Style-Writing-1zgye4&{query}&__hstc=14363112.4c7496d8370c0fedd2ec614ad3b4b31f.1698408367010.1698737477922.1698739703142.15&__hssc=14363112.18.1698739703142&__hsfp=2413774647"
    },
    {
      "name": "Constructing prompts - Instruction",
      "max_tokens": 500,
      "temperature": 0.5,
      "stop_sequences": [],
      "prompt": "Write a creative product description for a wireless headphone product named the CO-1T",
      "expected_output": "A revolution in sound, the CO-1T is the world's first truly wireless headphone with an in-ear design. The CO-1T is the perfect balance between sound quality, design, and price. With its sleek and modern design, the CO-1T is the perfect accessory for your on-the-go lifestyle. The CO-1T features a powerful and clear sound, with a deep bass and a clear treble. The CO-1T is also equipped with a noise-canceling microphone, so you can take calls and talk to your friends without any distractions. The CO-1T is the perfect choice for anyone who wants a high-quality and affordable wireless headphone.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - Specifics",
      "max_tokens": 500,
      "temperature": 0.5,
      "stop_sequences": [],
      "prompt": """Write a creative product description for a wireless headphone product named the CO-1T with the keywords "bluetooth", "wireless", "fast charging" for a software developer who works in noisy offices, and describe benefits of this product.""",
      "expected_output": "Do you hate noisy work environments? Well, we got a great solution for you! The CO-1T is the perfect wireless headphone for software developers who work in loud and disruptive offices. With its bluetooth connectivity and noise-canceling features, you can stay focused on your work without any distractions.  Our product also has fast charging, so you won't have to worry about battery life. Instead, you can quickly get back to work in no time. So what are you waiting for? Become the most productive person in your office with the help of the CO-1T.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - Structured",
      "max_tokens": 500,
      "temperature": 0.5,
      "stop_sequences": [],
      "prompt": """Write a creative product description for a wireless headphone product named the CO-1T.
Keywords: "bluetooth", "wireless", "fast charging"
Audience: a software developer who works in noisy offices
Describe: benefits of this product""",
      "expected_output": "Think back to the last time you were working without any distractions in the office. That's right...I bet it's been a while. With the newly improved CO-1T noise-cancelling Bluetooth headphones, you can work in peace all day. Designed in partnership with software developers who work around the mayhem of tech startups, these headphones are finally the break you've been waiting for. With fast charging capacity, you never have to worry about being tied down to a wall again. Instead, you can quickly get back to work in no time. The CO-1T: the perfect partner for any software developer who wants to be productive in a chaotic world.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - Without Context",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": "What are the key features of the CO-1T wireless headphone",
      "expected_output": "The CO-1T wireless headphone is a high-quality, comfortable, and durable headphone that is designed for use with a variety of devices. It features a sleek and modern design, a comfortable and secure fit, and a high-quality sound. The CO-1T is also equipped with a variety of features, including a built-in microphone, a multi-function button, and a rechargeable battery.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - With Context",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """Think back to the last time you were working without any distractions in the office. That's right...I bet it's been a while. \
With the newly improved CO-1T noise-cancelling Bluetooth headphones, you can work in peace all day. Designed in partnership with \
software developers who work around the mayhem of tech startups, these headphones are finally the break you've been waiting for. With \
fast charging capacity and wireless Bluetooth connectivity, the CO-1T is the easy breezy way to get through your day without being \
overwhelmed by the chaos of the world.
Given the information above, answer this question: What are the key features of the CO-1T wireless headphone""",
      "expected_output": "The answer is The CO-1T wireless headphones are designed to be noise-cancelling and Bluetooth enabled. They are also designed to be fast charging and have wireless Bluetooth connectivity.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - Without Examples",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """Turn the following message to a virtual assistant into the correct action:
Send a message to Alison to ask if she can pick me up tonight to go to the concert together""",
      "expected_output": """Here is the message to Alison:

Hey Alison, I hope you're doing well! I was wondering if you could pick me up tonight to go to the concert together. I would really appreciate it, and I think it would be a lot of fun. Let me know if you're able to do this, and I'll make sure to be ready on time.

Thanks,

[Your Name]""",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - With Examples",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """Turn the following message to a virtual assistant into the correct action:

Message: Ask my aunt if she can go to the JDRF Walk with me October 6th
Action: can you go to the jdrf walk with me october 6th

Message: Ask Eliza what should I bring to the wedding tomorrow
Action: what should I bring to the wedding tomorrow

Message: Send message to supervisor that I am sick and will not be in today
Action: I am sick and will not be in today

Message: Send a message to Alison to ask if she can pick me up tonight to go to the concert together""",
      "expected_output": "Can you pick me up tonight to go to the concert together?",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - Without Examples (Chain of Thought)",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. \
How many tennis balls does he have now?
A: The answer is 11.
Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?
A:""",
      "expected_output": "The answer is 29.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - With Examples (Chain of Thought)",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. \
How many tennis balls does he have now?
A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. \
The answer is 11.
Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?
A:""",
      "expected_output": "The cafeteria started with 23 apples. They used 20 to make lunch, so they have 23 - 20 = 3 apples. They bought 6 more apples, so they have 3 + 6 = 9 apples. The answer is 9.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - Table Format",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """Turn the following information into a table with columns Invoice Number, Merchant Name, and Account Number.
Bank Invoice: INVOICE #0521 MERCHANT ALLBIRDS ACC XXX3846
Bank Invoice: INVOICE #6781 MERCHANT SHOPPERS ACC XXX9877
Bank Invoice: INVOICE #0777 MERCHANT CN TOWER ACC XXX3846
""",
      "expected_output": """| Invoice Number | Merchant Name | Account Number |
|-----------|------------|-----------|
| 0521 | Allbirds | XXX3846 |
| 6781 | Shoppers | XXX9877 |
| 0777 | CN Tower | XXX3846 |""",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - JSON Format",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """Turn the following information into a JSON string with the following keys: Invoice Number, Merchant Name, and Account Number.
Bank Invoice: INVOICE #0521 MERCHANT ALLBIRDS ACC XXX3846
Bank Invoice: INVOICE #6781 MERCHANT SHOPPERS ACC XXX9877
Bank Invoice: INVOICE #0777 MERCHANT CN TOWER ACC XXX3846
""",
      "expected_output": """[
  {
    "Invoice Number": "0521",
    "Merchant Name": "Allbirds",
    "Account Number": "XXXX3846"
  },
  {
    "Invoice Number": "6781",
    "Merchant Name": "Shoppers",
    "Account Number": "XXXX9877"
  },
  {
    "Invoice Number": "0777",
    "Merchant Name": "CN Tower",
    "Account Number": "XXXX3846"
  }
]""",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - Without Steps",
      "max_tokens": 500,
      "temperature": 0.5,
      "stop_sequences": [],
      "prompt": "Generate a startup idea for this industry: education",
      "expected_output": "A mobile app that provides a platform for students to connect with each other and share resources.",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
    {
      "name": "Constructing prompts - With Prefix (Zero Shot Chain of Thought)",
      "max_tokens": 500,
      "temperature": 0,
      "stop_sequences": [],
      "prompt": """Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, \
how many apples do they have?
A: Let's think step by step.""",
      "expected_output": """The cafeteria started with 23 apples, used 20 to make lunch, and bought 6 more. To find out how many apples they have now, we can subtract 20 from the original number of apples, and then add 6. So, we have 23 - 20 + 6 = 9 apples.
So, the answer is 9.""",
      "doc_url": "https://docs.cohere.com/docs/constructing-prompts"
    },
]
