from dataclasses import dataclass


@dataclass
class A:

    class_attribute: str = "skip and pass"

    @classmethod
    def _get_favicon_path(cls, object_name: str):
        pass

    def get_tabs_info(self):
        pass
