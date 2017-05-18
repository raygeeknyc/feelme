from google.cloud import language

language_client = language.Client()

while True:
    text = raw_input("tell me something: ")
    if not text:
        break

    document = language_client.document_from_text(text)

    sentiment = document.analyze_sentiment().sentiment

    entities = document.analyze_entities().entities

    tokens = document.analyze_syntax().tokens

    print("Text: {}".format(text))
    if sentiment.score < 0:
        mood = "sad"
    elif sentiment.score > 0:
        mood = "glad"
    else:
        mood = "meh"
    print("Sentiment: {}: {}, {}".format(mood, sentiment.score, sentiment.magnitude))
    for entity in entities:
        print("Entity: {}: {}".format(entity.entity_type, entity.name))
        print("source: {}: {}".format(entity.metadata, entity.salience))

    for token in tokens:
        print("Token: {}: {}".format(token.part_of_speech, token.text_content))
