# LanguageDetection

Language detector used by Interaction Bot.

# Method

We made detection by dictionary and with ngram based method with fastText.
We also made a language priority (made by counting the number of detected language by Interaction Bot in 24 hours).
With discord, you could also use the language of the discord user interface send by the api to determine if a input is reliable (when reliabe is false).

# Output

Language code | reliability

