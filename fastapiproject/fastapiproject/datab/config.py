from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def DATABASE_URL(self):
        url = (
            'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
                self.POSTGRES_USER,
                self.POSTGRES_PASSWORD,
                'localhost',
                self.DB_PORT,
                self.POSTGRES_DB
            )
        )
        return url

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
