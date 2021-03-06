from pydantic import BaseSettings


class Settings(BaseSettings):
    development: bool = True

    # Anserini searcher settings
    index_path: str = 'lucene-index-covid-paragraph'
    max_docs: int = 96
    bm25_k1: float = 0.4
    bm25_b: float = 0.9
    rm3: bool = False
    rm3_fb_terms: int = 10
    rm3_fb_docs: int = 10
    rm3_original_query_weight: float = 0.5

    # T5 model settings
    t5_model_dir: str = 'gs://neural-covidex/data/t5_base/export/1585070383'
    t5_batch_size: int = 96
    t5_device: str = 'cuda:0'

    # Paragraph highlighting
    highlight = True
    highlight_max_paragraphs: int = 30
    highlight_device: str = 'cuda:1'

    # Response settings
    max_paragraphs_per_doc = 2

    class Config:
        env_file = '.env'


settings = Settings()
