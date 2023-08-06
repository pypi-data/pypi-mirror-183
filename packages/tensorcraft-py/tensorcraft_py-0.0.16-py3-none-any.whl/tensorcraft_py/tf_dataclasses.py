import typing
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from random import randint

from dataclasses_json import DataClassJsonMixin


class JobType(str, Enum):
  TEXT_2_IMAGE = "text2image"
  IMAGE_2_IMAGE = "image2image"

class JobState(str, Enum):
  UNKNOWN = "unknown"
  SUBMITTED = "submitted"
  ACCEPTED = "accepted"
  WORKING = "working"
  FINISHED = "finished"
  ERROR = "error"



@dataclass
class Text2ImageParams(DataClassJsonMixin):
  seed: int = randint(0, 1000000)


@dataclass
class ImageSize(DataClassJsonMixin):
  width: int
  height: int


@dataclass
class ImageData(DataClassJsonMixin):
  id: str

  size: ImageSize

  uri: typing.Optional[str] = None
  reported: bool = False
  

  user_secret_id: typing.Optional[str] = None
  prompt: typing.Optional[str] = None
  seed: typing.Optional[int] = None
  source_image_id: typing.Optional[str] = None
  job_id: typing.Optional[str] = None
  image_bytes: typing.Optional[bytearray] = None
  creation_time: datetime = datetime.now()


@dataclass
class JobStatus(DataClassJsonMixin):
  job_id: str
  job_state: JobState
  progress_pct: float
  images: list[ImageData] = field(default_factory=list)
  image_uris: list[str] = field(default_factory=list)
  error: bool = False


@dataclass
class Image2ImageParams(DataClassJsonMixin):
  source_image_id: str
  strength: float = 0.5
  seeds: typing.Optional[list[int]] = None


@dataclass
class Job(DataClassJsonMixin):
  id: str
  user_secret_id: str
  job_type: JobType
  prompt: str
  batch_size: int = 5
  size: ImageSize = ImageSize(512, 512)

  ddim_steps: int = 50
  scale: float = 7.5

  text2image_params: typing.Optional[Text2ImageParams] = None
  image2image_params: typing.Optional[Image2ImageParams] = None

  creation_time: datetime = datetime.now()
  reported: bool = False
  status: typing.Optional[JobStatus] = None



@dataclass
class FilterExample(DataClassJsonMixin):
  image_data: ImageData 
  filter_id: typing.Optional[str]=None
  source_image_data: typing.Optional[ImageData ]=None
  strength: float = 1.0
  tags: list[str]= field(default_factory=list)
  example_group: typing.Optional[str]=None # deprecated
  
@dataclass
class Filter(DataClassJsonMixin):
  id: str
  name: str
  description: str
  prompt: str
  
  ddim_steps: int
  scale: float 
  strength: float
  is_premium: bool = False
  user_secret_id: typing.Optional[str] = None
  creation_time: datetime = datetime.now()
  thumbnail_uri: typing.Optional[str] = None #deprecated
  examples: typing.Optional[list[FilterExample]] = None

@dataclass
class AppFilters(DataClassJsonMixin):
  app_id: str
  filters: list[Filter]
  
