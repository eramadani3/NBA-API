print(getwd())

# Load the hoopR package
library(hoopR)

# Set the range of draft years
draft_years <- 2006:2023

# Initialize an empty list to collect data by pick number
picks_list <- vector("list", length = 60)  # assuming up to 60 picks per draft

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

# Save the data to separate CSV files for each pick number
for (pick_number in 1:60) {
  print(paste0("Writing file: nba_draft_pick_", pick_number, ".csv"))  # Added print statement
  write.csv(picks_list[[pick_number]], file = paste0("nba_draft_pick_", pick_number, ".csv"), row.names = FALSE)
}
