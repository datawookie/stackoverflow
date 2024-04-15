

# RUN jupyter nbextension enable codefolding/main
# RUN jupyter nbextension enable toc2/main
# RUN jupyter nbextension enable scratchpad/main
# RUN jupyter nbextension enable collapsible_headings/main
# RUN jupyter nbextension enable highlight_selected_word/main

# RUN mkdir -p ~/.jupyter
# RUN echo "c.NotebookApp.ip = '*' "             >  ~/.jupyter/jupyter_notebook_config.py
# RUN echo "c.NotebookApp.open_browser = False " >> ~/.jupyter/jupyter_notebook_config.py
# RUN echo "c.NotebookApp.token = '' "           >> ~/.jupyter/jupyter_notebook_config.py

# # **this does not work!**
# RUN echo "c.NotebookApp.key_bindings = [ \n \
#   { 'command': 'jupyter-notebook:move-cell-up',   'keys': ['Alt-Up'] }, \n \
#   { 'command': 'jupyter-notebook:move-cell-down', 'keys': ['Alt-Down'] }]" >> ~/.jupyter/jupyter_notebook_config.py

# FROM python:3.9

# WORKDIR /usr/src/app

# RUN pip install --no-cache-dir \
#         notebook==6.4.8
#         # jupyter_contrib_nbextensions==0.5.1
#         # jupyter_server==1.13.5

# # RUN pip install  ipywidgets
# # RUN pip uninstall traitlets -y
# # RUN pip install traitlets==5.9.0
# # RUN pip install jupyter_contrib_nbextensions
# # RUN jupyter contrib nbextension install

# # RUN jupyter contrib nbextension install --user

# # RUN jupyter contrib nbextension install --user
# # RUN jupyter nbextensions_configurator enable --user

# EXPOSE 8888

# CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]


# # Use the official Python 3.9 image as a parent image
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /usr/src/app

# # Install Jupyter Notebook using pip
# RUN pip install --no-cache-dir notebook

# # Expose the port Jupyter Notebook will run on
# EXPOSE 8888

# # Run Jupyter Notebook when the container launches
# CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]

# # Use the official Python 3.9 image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Jupyter Notebook
RUN pip install --no-cache-dir notebook

# Install Jupyter contrib nbextensions
RUN pip install --no-cache-dir jupyter_contrib_nbextensions \
    && jupyter contrib nbextension install --user

# Install and enable the Jupyter Notebook configurator
RUN pip install jupyter_nbextensions_configurator \
    && jupyter nbextensions_configurator enable --user

# Expose the port Jupyter Notebook will run on
EXPOSE 8888

# Run Jupyter Notebook when the container launches
CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
