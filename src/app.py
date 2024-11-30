import streamlit as st
from services.blob_service import AzureBlobService
from services.credit_card_service import AzureCreditCardService
from models.credit_card_info import CreditCardInfo
from utils.logger import setup_logger

logger = setup_logger()

def configure_interface():
    st.title("Upload de Arquivo - Validação de Cartão de Crédito")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        file_name = uploaded_file.name
        blob_service = AzureBlobService()
        blob_url = blob_service.upload_file(uploaded_file, file_name)

        if blob_url:
            st.success(f"Arquivo '{file_name}' enviado com sucesso!")
            credit_card_service = AzureCreditCardService()
            credit_card_info = credit_card_service.detect_info(blob_url)

            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error("Erro ao enviar o arquivo para o Azure Blob Storage.")

def show_image_and_validation(blob_url: str, credit_card_info: CreditCardInfo):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validação:")

    if credit_card_info and credit_card_info.card_name:
        st.markdown("<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info.card_name}")
        st.write(f"Banco Emissor: {credit_card_info.bank_name}")
        st.write(f"Data de Validade: {credit_card_info.expiry_date}")
    else:
        st.markdown("<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")

if __name__ == "__main__":
    try:
        configure_interface()
    except Exception as e:
        logger.error(f"Erro na aplicação: {e}")
        st.error("Ocorreu um erro. Verifique os logs para mais detalhes.")
