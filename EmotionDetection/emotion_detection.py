import requests
import json


def emotion_detector( text_to_analyse ) :
    
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {
        "Content-Type" : "application/json",
        "grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"
    }
    DATA = {
        "raw_document" : { "text" : text_to_analyse }
    }

    try :

        response = requests.post( URL, headers = HEADERS, json = DATA )

        if( ( response.status_code >= 200 ) and ( response.status_code < 300 ) ) :

            response_data = json.loads( response.text )

            emotions = response_data[ "emotionPredictions" ][ 0 ][ "emotion" ]

            dominant_emotion = max( emotions, key = emotions.get )

            return {
                "anger" : emotions[ "anger" ],
                "disgust": emotions[ "disgust" ],
                "fear": emotions[ "fear" ],
                "joy": emotions[ "joy" ],
                "sadness": emotions[ "sadness" ],
                "dominant_emotion" : dominant_emotion
            }
        
        else :

            return { 
                "something went wrong" : response.status_code,
                "details about" : response.text
            }
    
    except requests.exceptions.RequestException as e :

        return { "exception" : str(e) }
    

# For testing in terminal:

if __name__ == "__main__" :
    
    text = input( "Enter the text for analyzing emotions...\n" )
    result = emotion_detector( text )
    print("Resultado del análisis de emociones: ", result )
