from mlproject2 import logger
from mlproject2.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline
from mlproject2.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject2.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject2.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlproject2.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation Stage"

try:
     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
     data_ingestion = DataTransformationTrainingPipeline()
     data_ingestion.main()
     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e