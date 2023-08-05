
from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class ImageDigest(BaseResourceCheck):

    def __init__(self):
        """
         The image specification should use a digest instead of a tag to make sure the container always uses the same
         version of the image.
         https://kubernetes.io/docs/concepts/configuration/overview/#container-images

         An admission controller could be used to enforce the use of image digest
         """
        name = "Image should use digest"
        id = "CKV_K8S_43"
        supported_resources = ["kubernetes_pod", "kubernetes_pod_v1",
                               "kubernetes_deployment", "kubernetes_deployment_v1"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf) -> CheckResult:
        spec = conf.get('spec', [None])[0]
        if spec:
            evaluated_keys_path = "spec"

            template = spec.get("template")
            if template and isinstance(template, list):
                template = template[0]
                template_spec = template.get("spec")
                if template_spec and isinstance(template_spec, list):
                    spec = template_spec[0]
                    evaluated_keys_path = f'{evaluated_keys_path}/[0]/template/[0]/spec'

            containers = spec.get("container")
            if containers is None:
                return CheckResult.UNKNOWN
            for idx, container in enumerate(containers):
                if not isinstance(container, dict):
                    return CheckResult.UNKNOWN
                if container.get("image") and isinstance(container.get("image"), list):
                    name = container.get("image")[0]
                    if "@" not in name:
                        self.evaluated_keys = [f'{evaluated_keys_path}/[0]/container/[{idx}]/image']
                        return CheckResult.FAILED
            return CheckResult.PASSED
        return CheckResult.FAILED


check = ImageDigest()
