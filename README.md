 gcloud build submit --tag gcr.io/diabetesdash/prediction-of-diabetes --project=diabetesdash
 
 gcloud run deploy --image gcr.io/diabetesdash/prediction-of-diabetes --platform manage
    --project=diabetesdash --allow-unauthenticated
    
 

