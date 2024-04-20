from pydantic import BaseModel, Field, PastDatetime


class Step(BaseModel):
    pass


class SubStep(Step):
    pass


class AlgorithmInfo(BaseModel):
    title: str
    description: str | None
    created_at: PastDatetime

    def __lt__(self, obj: "AlgorithmInfo"):
        if not isinstance(obj, AlgorithmInfo):
            return ValueError("This object itsn't a AlgorithmInfo")
        return self.created_at < obj.created_at


class Algorithm(BaseModel):
    steps: list[Step] = Field(default_factory=list)
    info: AlgorithmInfo

    def __lt__(self, obj: "Algorithm"):
        if not isinstance(obj, Algorithm):
            return ValueError("This object itsn't a Algorithm")
        return self.info < obj.info


class Library:
    algorithms: list[Algorithm]
