print(getwd())

# Load necessary libraries
library(hoopR)
library(mongolite)
library(jsonlite)
library(dotenv)

# Load environment variables from .env file located in the parent directory of the script
#dotenv::load_dot_env("../.env")  # Adjusted to point to the parent directory

# Set the range of draft years
draft_years <- 2000:2023

# Initialize an empty list to collect data by pick number
picks_list <- vector("list", length = 60)  # assuming up to 60 picks per draft

# Retrieve the MongoDB connection string from the .env file
mongo_url <- "mongodb+srv://eramadani:MQP123@mqp-database.3yyl9tm.mongodb.net/?retryWrites=true&w=majority"
collection_name <- "Nba_collection"

# Create a connection to the MongoDB collection
mongo_collection <- mongo(collection = collection_name, url = mongo_url)

# Loop through each draft year
for (year in draft_years) {
  # Get the draft data
  draft_data <- nba_drafthistory(season = year)
  draft_history_df <- draft_data$DraftHistory
  
  # Loop through each pick number
  for (pick_number in 1:60) {  # assuming up to 60 picks per draft
    pick_data <- subset(draft_history_df, OVERALL_PICK == pick_number)
    
    # Append the data to the corresponding list element
    if (is.null(picks_list[[pick_number]])) {
      picks_list[[pick_number]] <- pick_data
    } else {
      picks_list[[pick_number]] <- rbind(picks_list[[pick_number]], pick_data)
    }
  }
}

# Insert the data into MongoDB
for (pick_number in 1:60) {
  pick_data <- picks_list[[pick_number]]
  
  if (nrow(pick_data) > 0) {
    # Convert the data frame to JSON
    json_data <- toJSON(pick_data, auto_unbox = TRUE)
    
    # Attempt to insert the data into the MongoDB collection
    tryCatch({
      mongo_collection$insert(json_data)
      print(paste0("Uploaded data for pick number ", pick_number))
    }, error = function(e) {
      print(paste0("Failed to upload data for pick number ", pick_number, ": ", e$message))
    })
  }
}

# Close the connection
mongo_collection$disconnect()
