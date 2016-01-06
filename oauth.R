# Create an app on twitter and they will provide you client id and 
# client secret and you can use it to get the access token.
# package required : httr 

tweetOauth <- function(client_id = NULL, client_secret = NULL) {
  if (is.null(client_id) || is.null(client_secret)) {
    stop("Nither client_id nor client_secret can be NULL")
  }

  request   <- "https://api.twitter.com/oauth/request_token"
  authorize <- "https://api.twitter.com/oauth/authenticate"
  access    <-  "https://api.twitter.com/oauth/access_token"

  twitter <- httr::oauth_endpoint(request,authorize,access)
  myapp   <- httr::oauth_app("twitter", key = client_id, secret = client_secret)

  result <- try(token <- httr::oauth1.0_token(twitter, myapp))
  result <- class(result)
  if( result[1] == "try-error") {
    stop("Either internet connection is off or your argument(s) are incorrect")
  }
  token
}
