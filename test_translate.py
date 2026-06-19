from deep_translator import GoogleTranslator

result = GoogleTranslator(source="en", target="hi").translate("Hello, how are you?")
print(result)