<p align="center">
    <img src="https://github.com/dhmay/jamstats/blob/main/resources/jamstats_logo.png" width="300">
</p>

Tools for doing statistics and making plots on data from [CRG roller derby scoreboard](https://github.com/rollerderby/scoreboard) JSON files, or from a running scoreboard server. 

Various installation options, including a Windows executable that can build plots without using the command line. Supports both v4.x and v5.x scoreboard versions. 

* [Installation](#installation)
* [Usage](#usage)

## Let's see some plots!

If you like these plots, you might like this set of tools

![Cumulative points per jam, by team, in a derby game](https://github.com/dhmay/jamstats/blob/main/resources/cumulative_score_by_jam.png)
![Barplot of points per jam, by team, in a derby game](https://github.com/dhmay/jamstats/blob/main/resources/jam_points_barplot.png)
![Plots summarizign lead by team, in a derby game](https://github.com/dhmay/jamstats/blob/main/resources/lead_summary.png)
![Plots summarizing jammers by team, in a derby game](https://github.com/dhmay/jamstats/blob/main/resources/jammer_summary.png)
![Plots with individual anonymized jammer stats, in a derby game](https://github.com/dhmay/jamstats/blob/main/resources/jammer_stats.png)
![Plots with individual anonymized skater stats, in a derby game](https://github.com/dhmay/jamstats/blob/main/resources/skater_stats.png)

## Installation

#### Option 1: Windows executable

Go to the [latest release](https://github.com/dhmay/jamstats/releases) and download the file `jamstats.exe`.

#### Option 2: On any platform, with Python 3.7 or later

`pip install jamstats`

## Usage

### No-commandline option

On Windows, to generate a plots .pdf, you can simply drag your game JSON file onto the jamstats.exe file. That will generate a .pdf file in the same directory as your `.json` file, with the same name but with the `.json` extension replaced with `.pdf`.

### Commandline

Get full help for the `jamstats` command by running it with the `--help` argument.

`jamstats [-h] [--anonymize] [--debug] [--inprogress] jsonfileorserver [outfile]`

Makes plots describing a game and writes them to a PDF. If output PDF file isn't specified, uses the input filepath and changes .json to .pdf. If `--inprogress` is specified, instead of reading an input JSON file, connects to a running scoreboard server and downloads the current game state. In that case, the first unnamed argument should be a string of the format `server:port`, e.g., `localhost:8000`. 

If `outfile` has a `.txt` or `.tsv` extension, will instead write tab-delimited game data.

### Using jamstats from Python

This example Python code parses a scoreboard json file, writes it out as a TSV file, makes a bunch of plots and saves them to a PDF file.

```python
from jamstats.io.scoreboard_json_io import load_derby_game_from_json_file
from jamstats.plots import plot_together

in_json_filepath = "period2.json"
out_tsv_filepath = "jam_data.tsv"
out_pdf_filepath = "game_plots.pdf"

# parse a scoreboard json file
derby_game = load_derby_game_from_json_file(in_json_filepath)

# Write out a .tsv file with jam data.
tsv_io.write_game_data_tsv(derby_game, out_tsv_filepath)
                                       
# Write a .pdf with a bunch of plots
plot_together.save_game_plots_to_pdf(derby_game, out_pdf_filepath)
```
