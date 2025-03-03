import yaml

class Read_Config:

    _config_data = None  # 靜態變數，存放設定內容

    @staticmethod
    def load_config(file_path="config/config.yaml"):
        if Read_Config._config_data is None:
            with open(file_path, "r", encoding="utf-8") as file:
                Read_Config._config_data = yaml.safe_load(file)

    @staticmethod
    def get_admin_page_url():
        Read_Config.load_config()
        return Read_Config._config_data["admin_login_info"]["admin_page_url"]

    @staticmethod
    def get_username():
        Read_Config.load_config()
        return Read_Config._config_data["admin_login_info"]["username"]

    @staticmethod
    def get_password():
        Read_Config.load_config()
        return Read_Config._config_data["admin_login_info"]["password"]

    @staticmethod
    def get_invalid_username():
        Read_Config.load_config()
        return Read_Config._config_data["admin_login_info"]["invalid_username"]
