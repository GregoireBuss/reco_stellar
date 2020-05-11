mkdir streamlit-heroku

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/streamlit-heroku/config.toml
