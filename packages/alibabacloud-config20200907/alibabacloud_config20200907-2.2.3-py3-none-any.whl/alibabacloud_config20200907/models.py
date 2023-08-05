# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ResourceDirectoryFolderNode(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        children: List['ResourceDirectoryFolderNode'] = None,
        display_name: str = None,
        folder_id: str = None,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        self.account_id = account_id
        self.children = children
        self.display_name = display_name
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.parent_folder_id = parent_folder_id

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = ResourceDirectoryFolderNode()
                self.children.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class ActiveAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActiveAggregateConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = ActiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class ActiveAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: ActiveAggregateConfigRulesResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = ActiveAggregateConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ActiveAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActiveAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActiveAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachAggregateConfigRuleToCompliancePackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class AttachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[AttachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = AttachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class AttachAggregateConfigRuleToCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: AttachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = AttachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachAggregateConfigRuleToCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachAggregateConfigRuleToCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachAggregateConfigRuleToCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachConfigRuleToCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_ids: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class AttachConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachConfigRuleToCompliancePackResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[AttachConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = AttachConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class AttachConfigRuleToCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: AttachConfigRuleToCompliancePackResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = AttachConfigRuleToCompliancePackResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachConfigRuleToCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachConfigRuleToCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachConfigRuleToCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        des_aggregator_ids: str = None,
        src_aggregator_id: str = None,
        src_compliance_pack_ids: str = None,
    ):
        self.des_aggregator_ids = des_aggregator_ids
        self.src_aggregator_id = src_aggregator_id
        self.src_compliance_pack_ids = src_compliance_pack_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.des_aggregator_ids is not None:
            result['DesAggregatorIds'] = self.des_aggregator_ids
        if self.src_aggregator_id is not None:
            result['SrcAggregatorId'] = self.src_aggregator_id
        if self.src_compliance_pack_ids is not None:
            result['SrcCompliancePackIds'] = self.src_compliance_pack_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesAggregatorIds') is not None:
            self.des_aggregator_ids = m.get('DesAggregatorIds')
        if m.get('SrcAggregatorId') is not None:
            self.src_aggregator_id = m.get('SrcAggregatorId')
        if m.get('SrcCompliancePackIds') is not None:
            self.src_compliance_pack_ids = m.get('SrcCompliancePackIds')
        return self


class CopyCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        copy_rules_result: bool = None,
        request_id: str = None,
    ):
        self.copy_rules_result = copy_rules_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy_rules_result is not None:
            result['CopyRulesResult'] = self.copy_rules_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopyRulesResult') is not None:
            self.copy_rules_result = m.get('CopyRulesResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopyCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyConfigRulesRequest(TeaModel):
    def __init__(
        self,
        des_aggregator_ids: str = None,
        src_aggregator_id: str = None,
        src_config_rule_ids: str = None,
    ):
        self.des_aggregator_ids = des_aggregator_ids
        self.src_aggregator_id = src_aggregator_id
        self.src_config_rule_ids = src_config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.des_aggregator_ids is not None:
            result['DesAggregatorIds'] = self.des_aggregator_ids
        if self.src_aggregator_id is not None:
            result['SrcAggregatorId'] = self.src_aggregator_id
        if self.src_config_rule_ids is not None:
            result['SrcConfigRuleIds'] = self.src_config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesAggregatorIds') is not None:
            self.des_aggregator_ids = m.get('DesAggregatorIds')
        if m.get('SrcAggregatorId') is not None:
            self.src_aggregator_id = m.get('SrcAggregatorId')
        if m.get('SrcConfigRuleIds') is not None:
            self.src_config_rule_ids = m.get('SrcConfigRuleIds')
        return self


class CopyConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        copy_rules_result: bool = None,
        request_id: str = None,
    ):
        self.copy_rules_result = copy_rules_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy_rules_result is not None:
            result['CopyRulesResult'] = self.copy_rules_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopyRulesResult') is not None:
            self.copy_rules_result = m.get('CopyRulesResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopyConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class CreateAggregateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[CreateAggregateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        risk_level: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = CreateAggregateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class CreateAggregateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules: List[CreateAggregateCompliancePackRequestConfigRules] = None,
        default_enable: bool = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.config_rules = config_rules
        self.default_enable = default_enable
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.default_enable is not None:
            result['DefaultEnable'] = self.default_enable
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = CreateAggregateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('DefaultEnable') is not None:
            self.default_enable = m.get('DefaultEnable')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateAggregateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules_shrink: str = None,
        default_enable: bool = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.config_rules_shrink = config_rules_shrink
        self.default_enable = default_enable
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.default_enable is not None:
            result['DefaultEnable'] = self.default_enable
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('DefaultEnable') is not None:
            self.default_enable = m.get('DefaultEnable')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateAggregateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAggregateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAggregateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAggregateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregateConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_condition: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        return self


class CreateAggregateConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAggregateConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAggregateConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAggregateConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        folder_ids_scope: str = None,
        input_parameters: Dict[str, Any] = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_account_ids_scope = exclude_account_ids_scope
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.folder_ids_scope = folder_ids_scope
        self.input_parameters = input_parameters
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.source_identifier = source_identifier
        self.source_owner = source_owner
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_account_ids_scope is not None:
            result['ExcludeAccountIdsScope'] = self.exclude_account_ids_scope
        if self.exclude_folder_ids_scope is not None:
            result['ExcludeFolderIdsScope'] = self.exclude_folder_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.folder_ids_scope is not None:
            result['FolderIdsScope'] = self.folder_ids_scope
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeAccountIdsScope') is not None:
            self.exclude_account_ids_scope = m.get('ExcludeAccountIdsScope')
        if m.get('ExcludeFolderIdsScope') is not None:
            self.exclude_folder_ids_scope = m.get('ExcludeFolderIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('FolderIdsScope') is not None:
            self.folder_ids_scope = m.get('FolderIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateAggregateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        folder_ids_scope: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_account_ids_scope = exclude_account_ids_scope
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.folder_ids_scope = folder_ids_scope
        self.input_parameters_shrink = input_parameters_shrink
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.source_identifier = source_identifier
        self.source_owner = source_owner
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_account_ids_scope is not None:
            result['ExcludeAccountIdsScope'] = self.exclude_account_ids_scope
        if self.exclude_folder_ids_scope is not None:
            result['ExcludeFolderIdsScope'] = self.exclude_folder_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.folder_ids_scope is not None:
            result['FolderIdsScope'] = self.folder_ids_scope
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeAccountIdsScope') is not None:
            self.exclude_account_ids_scope = m.get('ExcludeAccountIdsScope')
        if m.get('ExcludeFolderIdsScope') is not None:
            self.exclude_folder_ids_scope = m.get('ExcludeFolderIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('FolderIdsScope') is not None:
            self.folder_ids_scope = m.get('FolderIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateAggregateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAggregateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAggregateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAggregateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregateRemediationRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_id: str = None,
        invoke_type: str = None,
        params: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
        source_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.config_rule_id = config_rule_id
        self.invoke_type = invoke_type
        self.params = params
        self.remediation_template_id = remediation_template_id
        self.remediation_type = remediation_type
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.params is not None:
            result['Params'] = self.params
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class CreateAggregateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        request_id: str = None,
    ):
        self.remediation_id = remediation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAggregateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAggregateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAggregateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAggregatorRequestAggregatorAccounts(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class CreateAggregatorRequest(TeaModel):
    def __init__(
        self,
        aggregator_accounts: List[CreateAggregatorRequestAggregatorAccounts] = None,
        aggregator_name: str = None,
        aggregator_type: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.aggregator_accounts = aggregator_accounts
        self.aggregator_name = aggregator_name
        self.aggregator_type = aggregator_type
        self.client_token = client_token
        self.description = description

    def validate(self):
        if self.aggregator_accounts:
            for k in self.aggregator_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k.to_map() if k else None)
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k in m.get('AggregatorAccounts'):
                temp_model = CreateAggregatorRequestAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k))
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAggregatorShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_accounts_shrink: str = None,
        aggregator_name: str = None,
        aggregator_type: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.aggregator_accounts_shrink = aggregator_accounts_shrink
        self.aggregator_name = aggregator_name
        self.aggregator_type = aggregator_type
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_accounts_shrink is not None:
            result['AggregatorAccounts'] = self.aggregator_accounts_shrink
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorAccounts') is not None:
            self.aggregator_accounts_shrink = m.get('AggregatorAccounts')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAggregatorResponseBody(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        request_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAggregatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAggregatorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAggregatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class CreateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[CreateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        risk_level: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = CreateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class CreateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules: List[CreateCompliancePackRequestConfigRules] = None,
        default_enable: bool = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.config_rules = config_rules
        self.default_enable = default_enable
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.default_enable is not None:
            result['DefaultEnable'] = self.default_enable
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = CreateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('DefaultEnable') is not None:
            self.default_enable = m.get('DefaultEnable')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules_shrink: str = None,
        default_enable: bool = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.config_rules_shrink = config_rules_shrink
        self.default_enable = default_enable
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.default_enable is not None:
            result['DefaultEnable'] = self.default_enable
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('DefaultEnable') is not None:
            self.default_enable = m.get('DefaultEnable')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_condition: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
    ):
        self.client_token = client_token
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        return self


class CreateConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        input_parameters: Dict[str, Any] = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.input_parameters = input_parameters
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.source_identifier = source_identifier
        self.source_owner = source_owner
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.input_parameters_shrink = input_parameters_shrink
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.source_identifier = source_identifier
        self.source_owner = source_owner
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class CreateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
    ):
        self.client_token = client_token
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        return self


class CreateDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRemediationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_id: str = None,
        invoke_type: str = None,
        params: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
        source_type: str = None,
    ):
        self.client_token = client_token
        self.config_rule_id = config_rule_id
        self.invoke_type = invoke_type
        self.params = params
        self.remediation_template_id = remediation_template_id
        self.remediation_type = remediation_type
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.params is not None:
            result['Params'] = self.params
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class CreateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        request_id: str = None,
    ):
        self.remediation_id = remediation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactiveAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class DeactiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeactiveAggregateConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DeactiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DeactiveAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DeactiveAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: DeactiveAggregateConfigRulesResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = DeactiveAggregateConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeactiveAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeactiveAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeactiveAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactiveConfigRulesRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class DeactiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeactiveConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DeactiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DeactiveConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DeactiveConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: DeactiveConfigRulesResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = DeactiveConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeactiveConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeactiveConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeactiveConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregateCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_ids: str = None,
        delete_rule: bool = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.compliance_pack_ids = compliance_pack_ids
        self.delete_rule = delete_rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_ids is not None:
            result['CompliancePackIds'] = self.compliance_pack_ids
        if self.delete_rule is not None:
            result['DeleteRule'] = self.delete_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackIds') is not None:
            self.compliance_pack_ids = m.get('CompliancePackIds')
        if m.get('DeleteRule') is not None:
            self.delete_rule = m.get('DeleteRule')
        return self


class DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult(TeaModel):
    def __init__(
        self,
        operate_compliance_packs: List[DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks] = None,
    ):
        self.operate_compliance_packs = operate_compliance_packs

    def validate(self):
        if self.operate_compliance_packs:
            for k in self.operate_compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateCompliancePacks'] = []
        if self.operate_compliance_packs is not None:
            for k in self.operate_compliance_packs:
                result['OperateCompliancePacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_compliance_packs = []
        if m.get('OperateCompliancePacks') is not None:
            for k in m.get('OperateCompliancePacks'):
                temp_model = DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks()
                self.operate_compliance_packs.append(temp_model.from_map(k))
        return self


class DeleteAggregateCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        operate_compliance_packs_result: DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult = None,
        request_id: str = None,
    ):
        self.operate_compliance_packs_result = operate_compliance_packs_result
        self.request_id = request_id

    def validate(self):
        if self.operate_compliance_packs_result:
            self.operate_compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_compliance_packs_result is not None:
            result['OperateCompliancePacksResult'] = self.operate_compliance_packs_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateCompliancePacksResult') is not None:
            temp_model = DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult()
            self.operate_compliance_packs_result = temp_model.from_map(m['OperateCompliancePacksResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAggregateCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAggregateCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAggregateCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregateConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        delivery_channel_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class DeleteAggregateConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAggregateConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAggregateConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAggregateConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class DeleteAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAggregateConfigRulesResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DeleteAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DeleteAggregateConfigRulesResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DeleteAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: DeleteAggregateConfigRulesResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = DeleteAggregateConfigRulesResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregateRemediationsRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        remediation_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.remediation_ids = remediation_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.remediation_ids is not None:
            result['RemediationIds'] = self.remediation_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('RemediationIds') is not None:
            self.remediation_ids = m.get('RemediationIds')
        return self


class DeleteAggregateRemediationsResponseBodyRemediationDeleteResults(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        remediation_id: str = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.remediation_id = remediation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAggregateRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        remediation_delete_results: List[DeleteAggregateRemediationsResponseBodyRemediationDeleteResults] = None,
        request_id: str = None,
    ):
        self.remediation_delete_results = remediation_delete_results
        self.request_id = request_id

    def validate(self):
        if self.remediation_delete_results:
            for k in self.remediation_delete_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemediationDeleteResults'] = []
        if self.remediation_delete_results is not None:
            for k in self.remediation_delete_results:
                result['RemediationDeleteResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediation_delete_results = []
        if m.get('RemediationDeleteResults') is not None:
            for k in m.get('RemediationDeleteResults'):
                temp_model = DeleteAggregateRemediationsResponseBodyRemediationDeleteResults()
                self.remediation_delete_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAggregateRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAggregateRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAggregateRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAggregatorsRequest(TeaModel):
    def __init__(
        self,
        aggregator_ids: str = None,
        client_token: str = None,
    ):
        self.aggregator_ids = aggregator_ids
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_ids is not None:
            result['AggregatorIds'] = self.aggregator_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorIds') is not None:
            self.aggregator_ids = m.get('AggregatorIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.aggregator_id = aggregator_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAggregatorsResponseBodyOperateAggregatorsResult(TeaModel):
    def __init__(
        self,
        operate_aggregators: List[DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators] = None,
    ):
        self.operate_aggregators = operate_aggregators

    def validate(self):
        if self.operate_aggregators:
            for k in self.operate_aggregators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateAggregators'] = []
        if self.operate_aggregators is not None:
            for k in self.operate_aggregators:
                result['OperateAggregators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_aggregators = []
        if m.get('OperateAggregators') is not None:
            for k in m.get('OperateAggregators'):
                temp_model = DeleteAggregatorsResponseBodyOperateAggregatorsResultOperateAggregators()
                self.operate_aggregators.append(temp_model.from_map(k))
        return self


class DeleteAggregatorsResponseBody(TeaModel):
    def __init__(
        self,
        operate_aggregators_result: DeleteAggregatorsResponseBodyOperateAggregatorsResult = None,
        request_id: str = None,
    ):
        self.operate_aggregators_result = operate_aggregators_result
        self.request_id = request_id

    def validate(self):
        if self.operate_aggregators_result:
            self.operate_aggregators_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_aggregators_result is not None:
            result['OperateAggregatorsResult'] = self.operate_aggregators_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateAggregatorsResult') is not None:
            temp_model = DeleteAggregatorsResponseBodyOperateAggregatorsResult()
            self.operate_aggregators_result = temp_model.from_map(m['OperateAggregatorsResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAggregatorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAggregatorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAggregatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compliance_pack_ids: str = None,
        delete_rule: bool = None,
    ):
        self.client_token = client_token
        self.compliance_pack_ids = compliance_pack_ids
        self.delete_rule = delete_rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_ids is not None:
            result['CompliancePackIds'] = self.compliance_pack_ids
        if self.delete_rule is not None:
            result['DeleteRule'] = self.delete_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackIds') is not None:
            self.compliance_pack_ids = m.get('CompliancePackIds')
        if m.get('DeleteRule') is not None:
            self.delete_rule = m.get('DeleteRule')
        return self


class DeleteCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCompliancePacksResponseBodyOperateCompliancePacksResult(TeaModel):
    def __init__(
        self,
        operate_compliance_packs: List[DeleteCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks] = None,
    ):
        self.operate_compliance_packs = operate_compliance_packs

    def validate(self):
        if self.operate_compliance_packs:
            for k in self.operate_compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateCompliancePacks'] = []
        if self.operate_compliance_packs is not None:
            for k in self.operate_compliance_packs:
                result['OperateCompliancePacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_compliance_packs = []
        if m.get('OperateCompliancePacks') is not None:
            for k in m.get('OperateCompliancePacks'):
                temp_model = DeleteCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks()
                self.operate_compliance_packs.append(temp_model.from_map(k))
        return self


class DeleteCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        operate_compliance_packs_result: DeleteCompliancePacksResponseBodyOperateCompliancePacksResult = None,
        request_id: str = None,
    ):
        self.operate_compliance_packs_result = operate_compliance_packs_result
        self.request_id = request_id

    def validate(self):
        if self.operate_compliance_packs_result:
            self.operate_compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_compliance_packs_result is not None:
            result['OperateCompliancePacksResult'] = self.operate_compliance_packs_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateCompliancePacksResult') is not None:
            temp_model = DeleteCompliancePacksResponseBodyOperateCompliancePacksResult()
            self.operate_compliance_packs_result = temp_model.from_map(m['OperateCompliancePacksResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class DeleteConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRemediationsRequest(TeaModel):
    def __init__(
        self,
        remediation_ids: str = None,
    ):
        self.remediation_ids = remediation_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_ids is not None:
            result['RemediationIds'] = self.remediation_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationIds') is not None:
            self.remediation_ids = m.get('RemediationIds')
        return self


class DeleteRemediationsResponseBodyRemediationDeleteResults(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        remediation_id: str = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.remediation_id = remediation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        remediation_delete_results: List[DeleteRemediationsResponseBodyRemediationDeleteResults] = None,
        request_id: str = None,
    ):
        self.remediation_delete_results = remediation_delete_results
        self.request_id = request_id

    def validate(self):
        if self.remediation_delete_results:
            for k in self.remediation_delete_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemediationDeleteResults'] = []
        if self.remediation_delete_results is not None:
            for k in self.remediation_delete_results:
                result['RemediationDeleteResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediation_delete_results = []
        if m.get('RemediationDeleteResults') is not None:
            for k in m.get('RemediationDeleteResults'):
                temp_model = DeleteRemediationsResponseBodyRemediationDeleteResults()
                self.remediation_delete_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachAggregateConfigRuleToCompliancePackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class DetachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DetachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DetachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DetachAggregateConfigRuleToCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: DetachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = DetachAggregateConfigRuleToCompliancePackResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachAggregateConfigRuleToCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachAggregateConfigRuleToCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachAggregateConfigRuleToCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachConfigRuleToCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_ids: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class DetachConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        self.config_rule_id = config_rule_id
        self.error_code = error_code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetachConfigRuleToCompliancePackResponseBodyOperateRuleResult(TeaModel):
    def __init__(
        self,
        operate_rule_item_list: List[DetachConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList] = None,
    ):
        self.operate_rule_item_list = operate_rule_item_list

    def validate(self):
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_rule_item_list = []
        if m.get('OperateRuleItemList') is not None:
            for k in m.get('OperateRuleItemList'):
                temp_model = DetachConfigRuleToCompliancePackResponseBodyOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        return self


class DetachConfigRuleToCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        operate_rule_result: DetachConfigRuleToCompliancePackResponseBodyOperateRuleResult = None,
        request_id: str = None,
    ):
        self.operate_rule_result = operate_rule_result
        self.request_id = request_id

    def validate(self):
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateRuleResult') is not None:
            temp_model = DetachConfigRuleToCompliancePackResponseBodyOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(m['OperateRuleResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachConfigRuleToCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachConfigRuleToCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachConfigRuleToCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluatePreConfigRulesRequestResourceEvaluateItemsRules(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        input_parameters: str = None,
    ):
        self.identifier = identifier
        self.input_parameters = input_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        return self


class EvaluatePreConfigRulesRequestResourceEvaluateItems(TeaModel):
    def __init__(
        self,
        resource_logical_id: str = None,
        resource_properties: str = None,
        resource_type: str = None,
        rules: List[EvaluatePreConfigRulesRequestResourceEvaluateItemsRules] = None,
    ):
        self.resource_logical_id = resource_logical_id
        self.resource_properties = resource_properties
        self.resource_type = resource_type
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_logical_id is not None:
            result['ResourceLogicalId'] = self.resource_logical_id
        if self.resource_properties is not None:
            result['ResourceProperties'] = self.resource_properties
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceLogicalId') is not None:
            self.resource_logical_id = m.get('ResourceLogicalId')
        if m.get('ResourceProperties') is not None:
            self.resource_properties = m.get('ResourceProperties')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = EvaluatePreConfigRulesRequestResourceEvaluateItemsRules()
                self.rules.append(temp_model.from_map(k))
        return self


class EvaluatePreConfigRulesRequest(TeaModel):
    def __init__(
        self,
        enable_managed_rules: bool = None,
        resource_evaluate_items: List[EvaluatePreConfigRulesRequestResourceEvaluateItems] = None,
    ):
        self.enable_managed_rules = enable_managed_rules
        self.resource_evaluate_items = resource_evaluate_items

    def validate(self):
        if self.resource_evaluate_items:
            for k in self.resource_evaluate_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_managed_rules is not None:
            result['EnableManagedRules'] = self.enable_managed_rules
        result['ResourceEvaluateItems'] = []
        if self.resource_evaluate_items is not None:
            for k in self.resource_evaluate_items:
                result['ResourceEvaluateItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableManagedRules') is not None:
            self.enable_managed_rules = m.get('EnableManagedRules')
        self.resource_evaluate_items = []
        if m.get('ResourceEvaluateItems') is not None:
            for k in m.get('ResourceEvaluateItems'):
                temp_model = EvaluatePreConfigRulesRequestResourceEvaluateItems()
                self.resource_evaluate_items.append(temp_model.from_map(k))
        return self


class EvaluatePreConfigRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        enable_managed_rules: bool = None,
        resource_evaluate_items_shrink: str = None,
    ):
        self.enable_managed_rules = enable_managed_rules
        self.resource_evaluate_items_shrink = resource_evaluate_items_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_managed_rules is not None:
            result['EnableManagedRules'] = self.enable_managed_rules
        if self.resource_evaluate_items_shrink is not None:
            result['ResourceEvaluateItems'] = self.resource_evaluate_items_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableManagedRules') is not None:
            self.enable_managed_rules = m.get('EnableManagedRules')
        if m.get('ResourceEvaluateItems') is not None:
            self.resource_evaluate_items_shrink = m.get('ResourceEvaluateItems')
        return self


class EvaluatePreConfigRulesResponseBodyResourceEvaluationsRules(TeaModel):
    def __init__(
        self,
        annotation: str = None,
        compliance_type: str = None,
        help_url: str = None,
        identifier: str = None,
    ):
        self.annotation = annotation
        self.compliance_type = compliance_type
        self.help_url = help_url
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.help_url is not None:
            result['HelpUrl'] = self.help_url
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class EvaluatePreConfigRulesResponseBodyResourceEvaluations(TeaModel):
    def __init__(
        self,
        resource_logical_id: str = None,
        resource_type: str = None,
        rules: List[EvaluatePreConfigRulesResponseBodyResourceEvaluationsRules] = None,
    ):
        self.resource_logical_id = resource_logical_id
        self.resource_type = resource_type
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_logical_id is not None:
            result['ResourceLogicalId'] = self.resource_logical_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceLogicalId') is not None:
            self.resource_logical_id = m.get('ResourceLogicalId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = EvaluatePreConfigRulesResponseBodyResourceEvaluationsRules()
                self.rules.append(temp_model.from_map(k))
        return self


class EvaluatePreConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_evaluations: List[EvaluatePreConfigRulesResponseBodyResourceEvaluations] = None,
    ):
        self.request_id = request_id
        self.resource_evaluations = resource_evaluations

    def validate(self):
        if self.resource_evaluations:
            for k in self.resource_evaluations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceEvaluations'] = []
        if self.resource_evaluations is not None:
            for k in self.resource_evaluations:
                result['ResourceEvaluations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_evaluations = []
        if m.get('ResourceEvaluations') is not None:
            for k in m.get('ResourceEvaluations'):
                temp_model = EvaluatePreConfigRulesResponseBodyResourceEvaluations()
                self.resource_evaluations.append(temp_model.from_map(k))
        return self


class EvaluatePreConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EvaluatePreConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EvaluatePreConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAggregateCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GenerateAggregateCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAggregateCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAggregateCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateAggregateCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAggregateConfigRulesReportRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class GenerateAggregateConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        report_id: str = None,
        request_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.report_id = report_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateAggregateConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAggregateConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateAggregateConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compliance_pack_id: str = None,
    ):
        self.client_token = client_token
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GenerateCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateConfigRulesReportRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_ids: str = None,
    ):
        self.client_token = client_token
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class GenerateConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        report_id: str = None,
        request_id: str = None,
    ):
        self.report_id = report_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateAccountComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        compliance_type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.compliance_type = compliance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        return self


class GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult(TeaModel):
    def __init__(
        self,
        account_compliances: List[GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances] = None,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        self.account_compliances = account_compliances
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count

    def validate(self):
        if self.account_compliances:
            for k in self.account_compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountCompliances'] = []
        if self.account_compliances is not None:
            for k in self.account_compliances:
                result['AccountCompliances'].append(k.to_map() if k else None)
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_compliances = []
        if m.get('AccountCompliances') is not None:
            for k in m.get('AccountCompliances'):
                temp_model = GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResultAccountCompliances()
                self.account_compliances.append(temp_model.from_map(k))
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAggregateAccountComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        account_compliance_result: GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult = None,
        request_id: str = None,
    ):
        self.account_compliance_result = account_compliance_result
        self.request_id = request_id

    def validate(self):
        if self.account_compliance_result:
            self.account_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_compliance_result is not None:
            result['AccountComplianceResult'] = self.account_compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountComplianceResult') is not None:
            temp_model = GetAggregateAccountComplianceByPackResponseBodyAccountComplianceResult()
            self.account_compliance_result = temp_model.from_map(m['AccountComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateAccountComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateAccountComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateAccountComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
        required: bool = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetAggregateCompliancePackResponseBodyCompliancePackConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        risk_level: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class GetAggregateCompliancePackResponseBodyCompliancePackScope(TeaModel):
    def __init__(
        self,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class GetAggregateCompliancePackResponseBodyCompliancePack(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules: List[GetAggregateCompliancePackResponseBodyCompliancePackConfigRules] = None,
        create_timestamp: int = None,
        description: str = None,
        risk_level: int = None,
        scope: GetAggregateCompliancePackResponseBodyCompliancePackScope = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.config_rules = config_rules
        self.create_timestamp = create_timestamp
        self.description = description
        self.risk_level = risk_level
        self.scope = scope
        self.status = status

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.scope is not None:
            result['Scope'] = self.scope.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = GetAggregateCompliancePackResponseBodyCompliancePackConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Scope') is not None:
            temp_model = GetAggregateCompliancePackResponseBodyCompliancePackScope()
            self.scope = temp_model.from_map(m['Scope'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAggregateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack: GetAggregateCompliancePackResponseBodyCompliancePack = None,
        request_id: str = None,
    ):
        self.compliance_pack = compliance_pack
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack:
            self.compliance_pack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack is not None:
            result['CompliancePack'] = self.compliance_pack.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePack') is not None:
            temp_model = GetAggregateCompliancePackResponseBodyCompliancePack()
            self.compliance_pack = temp_model.from_map(m['CompliancePack'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetAggregateCompliancePackReportResponseBodyCompliancePackReport(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        compliance_pack_id: str = None,
        report_create_timestamp: int = None,
        report_status: str = None,
        report_url: str = None,
    ):
        self.account_id = account_id
        self.compliance_pack_id = compliance_pack_id
        self.report_create_timestamp = report_create_timestamp
        self.report_status = report_status
        self.report_url = report_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        return self


class GetAggregateCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_report: GetAggregateCompliancePackReportResponseBodyCompliancePackReport = None,
        request_id: str = None,
    ):
        self.compliance_pack_report = compliance_pack_report
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack_report:
            self.compliance_pack_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_report is not None:
            result['CompliancePackReport'] = self.compliance_pack_report.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackReport') is not None:
            temp_model = GetAggregateCompliancePackReportResponseBodyCompliancePackReport()
            self.compliance_pack_report = temp_model.from_map(m['CompliancePackReport'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        delivery_channel_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class GetAggregateConfigDeliveryChannelResponseBodyDeliveryChannel(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        aggregator_id: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAggregateConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel: GetAggregateConfigDeliveryChannelResponseBodyDeliveryChannel = None,
        request_id: str = None,
    ):
        self.delivery_channel = delivery_channel
        self.request_id = request_id

    def validate(self):
        if self.delivery_channel:
            self.delivery_channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel is not None:
            result['DeliveryChannel'] = self.delivery_channel.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannel') is not None:
            temp_model = GetAggregateConfigDeliveryChannelResponseBodyDeliveryChannel()
            self.delivery_channel = temp_model.from_map(m['DeliveryChannel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleCompliance(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus(TeaModel):
    def __init__(
        self,
        first_activated_timestamp: int = None,
        first_evaluation_started: bool = None,
        last_error_code: str = None,
        last_error_message: str = None,
        last_failed_evaluation_timestamp: int = None,
        last_failed_invocation_timestamp: int = None,
        last_successful_evaluation_timestamp: int = None,
        last_successful_invocation_timestamp: int = None,
    ):
        self.first_activated_timestamp = first_activated_timestamp
        self.first_evaluation_started = first_evaluation_started
        self.last_error_code = last_error_code
        self.last_error_message = last_error_message
        self.last_failed_evaluation_timestamp = last_failed_evaluation_timestamp
        self.last_failed_invocation_timestamp = last_failed_invocation_timestamp
        self.last_successful_evaluation_timestamp = last_successful_evaluation_timestamp
        self.last_successful_invocation_timestamp = last_successful_invocation_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_activated_timestamp is not None:
            result['FirstActivatedTimestamp'] = self.first_activated_timestamp
        if self.first_evaluation_started is not None:
            result['FirstEvaluationStarted'] = self.first_evaluation_started
        if self.last_error_code is not None:
            result['LastErrorCode'] = self.last_error_code
        if self.last_error_message is not None:
            result['LastErrorMessage'] = self.last_error_message
        if self.last_failed_evaluation_timestamp is not None:
            result['LastFailedEvaluationTimestamp'] = self.last_failed_evaluation_timestamp
        if self.last_failed_invocation_timestamp is not None:
            result['LastFailedInvocationTimestamp'] = self.last_failed_invocation_timestamp
        if self.last_successful_evaluation_timestamp is not None:
            result['LastSuccessfulEvaluationTimestamp'] = self.last_successful_evaluation_timestamp
        if self.last_successful_invocation_timestamp is not None:
            result['LastSuccessfulInvocationTimestamp'] = self.last_successful_invocation_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstActivatedTimestamp') is not None:
            self.first_activated_timestamp = m.get('FirstActivatedTimestamp')
        if m.get('FirstEvaluationStarted') is not None:
            self.first_evaluation_started = m.get('FirstEvaluationStarted')
        if m.get('LastErrorCode') is not None:
            self.last_error_code = m.get('LastErrorCode')
        if m.get('LastErrorMessage') is not None:
            self.last_error_message = m.get('LastErrorMessage')
        if m.get('LastFailedEvaluationTimestamp') is not None:
            self.last_failed_evaluation_timestamp = m.get('LastFailedEvaluationTimestamp')
        if m.get('LastFailedInvocationTimestamp') is not None:
            self.last_failed_invocation_timestamp = m.get('LastFailedInvocationTimestamp')
        if m.get('LastSuccessfulEvaluationTimestamp') is not None:
            self.last_successful_evaluation_timestamp = m.get('LastSuccessfulEvaluationTimestamp')
        if m.get('LastSuccessfulInvocationTimestamp') is not None:
            self.last_successful_invocation_timestamp = m.get('LastSuccessfulInvocationTimestamp')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleCreateBy(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        aggregator_name: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        creator_id: str = None,
        creator_name: str = None,
        creator_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.creator_type = creator_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails(TeaModel):
    def __init__(
        self,
        event_source: str = None,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleManagedRule(TeaModel):
    def __init__(
        self,
        compulsory_input_parameter_details: Dict[str, Any] = None,
        description: str = None,
        identifier: str = None,
        labels: List[str] = None,
        managed_rule_name: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        source_details: List[GetAggregateConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails] = None,
    ):
        self.compulsory_input_parameter_details = compulsory_input_parameter_details
        self.description = description
        self.identifier = identifier
        self.labels = labels
        self.managed_rule_name = managed_rule_name
        self.optional_input_parameter_details = optional_input_parameter_details
        self.source_details = source_details

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        if self.description is not None:
            result['Description'] = self.description
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name
        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')
        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetAggregateConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleSourceSourceDetails(TeaModel):
    def __init__(
        self,
        event_source: str = None,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class GetAggregateConfigRuleResponseBodyConfigRuleSource(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        owner: str = None,
        source_details: List[GetAggregateConfigRuleResponseBodyConfigRuleSourceSourceDetails] = None,
    ):
        self.identifier = identifier
        self.owner = owner
        self.source_details = source_details

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.owner is not None:
            result['Owner'] = self.owner
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetAggregateConfigRuleResponseBodyConfigRuleSourceSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        return self


class GetAggregateConfigRuleResponseBodyConfigRule(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        compliance: GetAggregateConfigRuleResponseBodyConfigRuleCompliance = None,
        config_rule_arn: str = None,
        config_rule_evaluation_status: GetAggregateConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_state: str = None,
        config_rule_trigger_types: str = None,
        create_by: GetAggregateConfigRuleResponseBodyConfigRuleCreateBy = None,
        create_timestamp: int = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        folder_ids_scope: str = None,
        input_parameters: Dict[str, Any] = None,
        managed_rule: GetAggregateConfigRuleResponseBodyConfigRuleManagedRule = None,
        maximum_execution_frequency: str = None,
        modified_timestamp: int = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope: str = None,
        risk_level: int = None,
        source: GetAggregateConfigRuleResponseBodyConfigRuleSource = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.account_id = account_id
        self.compliance = compliance
        self.config_rule_arn = config_rule_arn
        self.config_rule_evaluation_status = config_rule_evaluation_status
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_state = config_rule_state
        self.config_rule_trigger_types = config_rule_trigger_types
        self.create_by = create_by
        self.create_timestamp = create_timestamp
        self.description = description
        self.exclude_account_ids_scope = exclude_account_ids_scope
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.folder_ids_scope = folder_ids_scope
        self.input_parameters = input_parameters
        self.managed_rule = managed_rule
        self.maximum_execution_frequency = maximum_execution_frequency
        self.modified_timestamp = modified_timestamp
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.source = source
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        if self.compliance:
            self.compliance.validate()
        if self.config_rule_evaluation_status:
            self.config_rule_evaluation_status.validate()
        if self.create_by:
            self.create_by.validate()
        if self.managed_rule:
            self.managed_rule.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.config_rule_evaluation_status is not None:
            result['ConfigRuleEvaluationStatus'] = self.config_rule_evaluation_status.to_map()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_account_ids_scope is not None:
            result['ExcludeAccountIdsScope'] = self.exclude_account_ids_scope
        if self.exclude_folder_ids_scope is not None:
            result['ExcludeFolderIdsScope'] = self.exclude_folder_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.folder_ids_scope is not None:
            result['FolderIdsScope'] = self.folder_ids_scope
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Compliance') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleCompliance()
            self.compliance = temp_model.from_map(m['Compliance'])
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ConfigRuleEvaluationStatus') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus()
            self.config_rule_evaluation_status = temp_model.from_map(m['ConfigRuleEvaluationStatus'])
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('CreateBy') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeAccountIdsScope') is not None:
            self.exclude_account_ids_scope = m.get('ExcludeAccountIdsScope')
        if m.get('ExcludeFolderIdsScope') is not None:
            self.exclude_folder_ids_scope = m.get('ExcludeFolderIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('FolderIdsScope') is not None:
            self.folder_ids_scope = m.get('FolderIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('ManagedRule') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleManagedRule()
            self.managed_rule = temp_model.from_map(m['ManagedRule'])
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Source') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRuleSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class GetAggregateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule: GetAggregateConfigRuleResponseBodyConfigRule = None,
        request_id: str = None,
    ):
        self.config_rule = config_rule
        self.request_id = request_id

    def validate(self):
        if self.config_rule:
            self.config_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule is not None:
            result['ConfigRule'] = self.config_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRule') is not None:
            temp_model = GetAggregateConfigRuleResponseBodyConfigRule()
            self.config_rule = temp_model.from_map(m['ConfigRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRuleComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
    ):
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        return self


class GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_compliances: List[GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances] = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_compliances = config_rule_compliances
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count

    def validate(self):
        if self.config_rule_compliances:
            for k in self.config_rule_compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        result['ConfigRuleCompliances'] = []
        if self.config_rule_compliances is not None:
            for k in self.config_rule_compliances:
                result['ConfigRuleCompliances'].append(k.to_map() if k else None)
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        self.config_rule_compliances = []
        if m.get('ConfigRuleCompliances') is not None:
            for k in m.get('ConfigRuleCompliances'):
                temp_model = GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances()
                self.config_rule_compliances.append(temp_model.from_map(k))
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAggregateConfigRuleComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_compliance_result: GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult = None,
        request_id: str = None,
    ):
        self.config_rule_compliance_result = config_rule_compliance_result
        self.request_id = request_id

    def validate(self):
        if self.config_rule_compliance_result:
            self.config_rule_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_compliance_result is not None:
            result['ConfigRuleComplianceResult'] = self.config_rule_compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleComplianceResult') is not None:
            temp_model = GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult()
            self.config_rule_compliance_result = temp_model.from_map(m['ConfigRuleComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateConfigRuleComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateConfigRuleComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRuleComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRuleSummaryByRiskLevelRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
    ):
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregateConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries(TeaModel):
    def __init__(
        self,
        compliant_count: int = None,
        non_compliant_count: int = None,
        risk_level: int = None,
    ):
        self.compliant_count = compliant_count
        self.non_compliant_count = non_compliant_count
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class GetAggregateConfigRuleSummaryByRiskLevelResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_summaries: List[GetAggregateConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries] = None,
        request_id: str = None,
    ):
        self.config_rule_summaries = config_rule_summaries
        self.request_id = request_id

    def validate(self):
        if self.config_rule_summaries:
            for k in self.config_rule_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigRuleSummaries'] = []
        if self.config_rule_summaries is not None:
            for k in self.config_rule_summaries:
                result['ConfigRuleSummaries'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_summaries = []
        if m.get('ConfigRuleSummaries') is not None:
            for k in m.get('ConfigRuleSummaries'):
                temp_model = GetAggregateConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries()
                self.config_rule_summaries.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateConfigRuleSummaryByRiskLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateConfigRuleSummaryByRiskLevelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRuleSummaryByRiskLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateConfigRulesReportRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        report_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class GetAggregateConfigRulesReportResponseBodyConfigRulesReport(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        report_create_timestamp: int = None,
        report_id: str = None,
        report_status: str = None,
        report_url: str = None,
    ):
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.report_create_timestamp = report_create_timestamp
        self.report_id = report_id
        self.report_status = report_status
        self.report_url = report_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        return self


class GetAggregateConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        config_rules_report: GetAggregateConfigRulesReportResponseBodyConfigRulesReport = None,
        request_id: str = None,
    ):
        self.config_rules_report = config_rules_report
        self.request_id = request_id

    def validate(self):
        if self.config_rules_report:
            self.config_rules_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rules_report is not None:
            result['ConfigRulesReport'] = self.config_rules_report.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRulesReport') is not None:
            temp_model = GetAggregateConfigRulesReportResponseBodyConfigRulesReport()
            self.config_rules_report = temp_model.from_map(m['ConfigRulesReport'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateDiscoveredResourceRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        region: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.region = region
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetAggregateDiscoveredResourceResponseBodyDiscoveredResourceDetail(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        configuration: str = None,
        region: str = None,
        resource_creation_time: int = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.configuration = configuration
        self.region = region
        self.resource_creation_time = resource_creation_time
        self.resource_deleted = resource_deleted
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetAggregateDiscoveredResourceResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_detail: GetAggregateDiscoveredResourceResponseBodyDiscoveredResourceDetail = None,
        request_id: str = None,
    ):
        self.discovered_resource_detail = discovered_resource_detail
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_detail:
            self.discovered_resource_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discovered_resource_detail is not None:
            result['DiscoveredResourceDetail'] = self.discovered_resource_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceDetail') is not None:
            temp_model = GetAggregateDiscoveredResourceResponseBodyDiscoveredResourceDetail()
            self.discovered_resource_detail = temp_model.from_map(m['DiscoveredResourceDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateDiscoveredResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateDiscoveredResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateDiscoveredResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceByConfigRuleRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_type: str = None,
        config_rule_id: str = None,
        resource_owner_id: int = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        compliances: List[GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances] = None,
        total_count: int = None,
    ):
        self.compliances = compliances
        self.total_count = total_count

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances()
                self.compliances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAggregateResourceComplianceByConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetAggregateResourceComplianceByConfigRuleResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateResourceComplianceByConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceComplianceByConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceByConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAggregateResourceComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_result: GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult = None,
    ):
        self.request_id = request_id
        self.resource_compliance_result = resource_compliance_result

    def validate(self):
        if self.resource_compliance_result:
            self.resource_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_compliance_result is not None:
            result['ResourceComplianceResult'] = self.resource_compliance_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceComplianceResult') is not None:
            temp_model = GetAggregateResourceComplianceByPackResponseBodyResourceComplianceResult()
            self.resource_compliance_result = temp_model.from_map(m['ResourceComplianceResult'])
        return self


class GetAggregateResourceComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceGroupByRegionRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList(TeaModel):
    def __init__(
        self,
        compliances: List[GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances] = None,
        region_id: str = None,
    ):
        self.compliances = compliances
        self.region_id = region_id

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances()
                self.compliances.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_result_list: List[GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList] = None,
    ):
        self.compliance_result_list = compliance_result_list

    def validate(self):
        if self.compliance_result_list:
            for k in self.compliance_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplianceResultList'] = []
        if self.compliance_result_list is not None:
            for k in self.compliance_result_list:
                result['ComplianceResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_result_list = []
        if m.get('ComplianceResultList') is not None:
            for k in m.get('ComplianceResultList'):
                temp_model = GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList()
                self.compliance_result_list.append(temp_model.from_map(k))
        return self


class GetAggregateResourceComplianceGroupByRegionResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetAggregateResourceComplianceGroupByRegionResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateResourceComplianceGroupByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceComplianceGroupByRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceGroupByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceGroupByResourceTypeRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultListCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultList(TeaModel):
    def __init__(
        self,
        compliances: List[GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultListCompliances] = None,
        resource_type: str = None,
    ):
        self.compliances = compliances
        self.resource_type = resource_type

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultListCompliances()
                self.compliances.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_result_list: List[GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultList] = None,
    ):
        self.compliance_result_list = compliance_result_list

    def validate(self):
        if self.compliance_result_list:
            for k in self.compliance_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplianceResultList'] = []
        if self.compliance_result_list is not None:
            for k in self.compliance_result_list:
                result['ComplianceResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_result_list = []
        if m.get('ComplianceResultList') is not None:
            for k in m.get('ComplianceResultList'):
                temp_model = GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultList()
                self.compliance_result_list.append(temp_model.from_map(k))
        return self


class GetAggregateResourceComplianceGroupByResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetAggregateResourceComplianceGroupByResourceTypeResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateResourceComplianceGroupByResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceComplianceGroupByResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceGroupByResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceComplianceTimelineRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        start_time: int = None,
    ):
        self.aggregator_id = aggregator_id
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        availability_zone: str = None,
        capture_time: int = None,
        configuration: str = None,
        configuration_diff: str = None,
        region: str = None,
        resource_create_time: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.capture_time = capture_time
        self.configuration = configuration
        self.configuration_diff = configuration_diff
        self.region = region
        self.resource_create_time = resource_create_time
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline(TeaModel):
    def __init__(
        self,
        compliance_list: List[GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.compliance_list = compliance_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.compliance_list:
            for k in self.compliance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k in self.compliance_list:
                result['ComplianceList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_list = []
        if m.get('ComplianceList') is not None:
            for k in m.get('ComplianceList'):
                temp_model = GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList()
                self.compliance_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetAggregateResourceComplianceTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_timeline: GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline = None,
    ):
        self.request_id = request_id
        self.resource_compliance_timeline = resource_compliance_timeline

    def validate(self):
        if self.resource_compliance_timeline:
            self.resource_compliance_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_compliance_timeline is not None:
            result['ResourceComplianceTimeline'] = self.resource_compliance_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceComplianceTimeline') is not None:
            temp_model = GetAggregateResourceComplianceTimelineResponseBodyResourceComplianceTimeline()
            self.resource_compliance_timeline = temp_model.from_map(m['ResourceComplianceTimeline'])
        return self


class GetAggregateResourceComplianceTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceComplianceTimelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceComplianceTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceConfigurationTimelineRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        start_time: int = None,
    ):
        self.aggregator_id = aggregator_id
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        capture_time: str = None,
        configuration_diff: str = None,
        region: str = None,
        resource_create_time: str = None,
        resource_event_type: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.region = region
        self.resource_create_time = resource_create_time
        self.resource_event_type = resource_event_type
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.resource_event_type is not None:
            result['ResourceEventType'] = self.resource_event_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('ResourceEventType') is not None:
            self.resource_event_type = m.get('ResourceEventType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline(TeaModel):
    def __init__(
        self,
        configuration_list: List[GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.configuration_list = configuration_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.configuration_list:
            for k in self.configuration_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigurationList'] = []
        if self.configuration_list is not None:
            for k in self.configuration_list:
                result['ConfigurationList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration_list = []
        if m.get('ConfigurationList') is not None:
            for k in m.get('ConfigurationList'):
                temp_model = GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList()
                self.configuration_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetAggregateResourceConfigurationTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_configuration_timeline: GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline = None,
    ):
        self.request_id = request_id
        self.resource_configuration_timeline = resource_configuration_timeline

    def validate(self):
        if self.resource_configuration_timeline:
            self.resource_configuration_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_configuration_timeline is not None:
            result['ResourceConfigurationTimeline'] = self.resource_configuration_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceConfigurationTimeline') is not None:
            temp_model = GetAggregateResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline()
            self.resource_configuration_timeline = temp_model.from_map(m['ResourceConfigurationTimeline'])
        return self


class GetAggregateResourceConfigurationTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceConfigurationTimelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceConfigurationTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceCountsGroupByRegionRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        folder_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.folder_id = folder_id
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetAggregateResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        region: str = None,
        resource_count: int = None,
    ):
        self.group_name = group_name
        self.region = region
        self.resource_count = resource_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        return self


class GetAggregateResourceCountsGroupByRegionResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_counts_summary: List[GetAggregateResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary] = None,
        request_id: str = None,
    ):
        self.discovered_resource_counts_summary = discovered_resource_counts_summary
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetAggregateResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateResourceCountsGroupByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceCountsGroupByRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceCountsGroupByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregateResourceCountsGroupByResourceTypeRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        folder_id: str = None,
        region: str = None,
        resource_owner_id: int = None,
    ):
        self.aggregator_id = aggregator_id
        self.folder_id = folder_id
        self.region = region
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetAggregateResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.group_name = group_name
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetAggregateResourceCountsGroupByResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_counts_summary: List[GetAggregateResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary] = None,
        request_id: str = None,
    ):
        self.discovered_resource_counts_summary = discovered_resource_counts_summary
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetAggregateResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregateResourceCountsGroupByResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregateResourceCountsGroupByResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregateResourceCountsGroupByResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAggregatorRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
    ):
        self.aggregator_id = aggregator_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        return self


class GetAggregatorResponseBodyAggregatorAggregatorAccounts(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
        recorder_status: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type
        self.recorder_status = recorder_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.recorder_status is not None:
            result['RecorderStatus'] = self.recorder_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('RecorderStatus') is not None:
            self.recorder_status = m.get('RecorderStatus')
        return self


class GetAggregatorResponseBodyAggregator(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_account_count: int = None,
        aggregator_accounts: List[GetAggregatorResponseBodyAggregatorAggregatorAccounts] = None,
        aggregator_create_timestamp: str = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        aggregator_status: int = None,
        aggregator_type: str = None,
        description: str = None,
    ):
        self.account_id = account_id
        self.aggregator_account_count = aggregator_account_count
        self.aggregator_accounts = aggregator_accounts
        self.aggregator_create_timestamp = aggregator_create_timestamp
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.aggregator_status = aggregator_status
        self.aggregator_type = aggregator_type
        self.description = description

    def validate(self):
        if self.aggregator_accounts:
            for k in self.aggregator_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_account_count is not None:
            result['AggregatorAccountCount'] = self.aggregator_account_count
        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k.to_map() if k else None)
        if self.aggregator_create_timestamp is not None:
            result['AggregatorCreateTimestamp'] = self.aggregator_create_timestamp
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.aggregator_status is not None:
            result['AggregatorStatus'] = self.aggregator_status
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorAccountCount') is not None:
            self.aggregator_account_count = m.get('AggregatorAccountCount')
        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k in m.get('AggregatorAccounts'):
                temp_model = GetAggregatorResponseBodyAggregatorAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k))
        if m.get('AggregatorCreateTimestamp') is not None:
            self.aggregator_create_timestamp = m.get('AggregatorCreateTimestamp')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('AggregatorStatus') is not None:
            self.aggregator_status = m.get('AggregatorStatus')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetAggregatorResponseBody(TeaModel):
    def __init__(
        self,
        aggregator: GetAggregatorResponseBodyAggregator = None,
        request_id: str = None,
    ):
        self.aggregator = aggregator
        self.request_id = request_id

    def validate(self):
        if self.aggregator:
            self.aggregator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            temp_model = GetAggregatorResponseBodyAggregator()
            self.aggregator = temp_model.from_map(m['Aggregator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAggregatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAggregatorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAggregatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCompliancePackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
        required: bool = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetCompliancePackResponseBodyCompliancePackConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        risk_level: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class GetCompliancePackResponseBodyCompliancePackScope(TeaModel):
    def __init__(
        self,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class GetCompliancePackResponseBodyCompliancePack(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules: List[GetCompliancePackResponseBodyCompliancePackConfigRules] = None,
        create_timestamp: int = None,
        description: str = None,
        risk_level: int = None,
        scope: GetCompliancePackResponseBodyCompliancePackScope = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.config_rules = config_rules
        self.create_timestamp = create_timestamp
        self.description = description
        self.risk_level = risk_level
        self.scope = scope
        self.status = status

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.scope is not None:
            result['Scope'] = self.scope.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = GetCompliancePackResponseBodyCompliancePackConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Scope') is not None:
            temp_model = GetCompliancePackResponseBodyCompliancePackScope()
            self.scope = temp_model.from_map(m['Scope'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack: GetCompliancePackResponseBodyCompliancePack = None,
        request_id: str = None,
    ):
        self.compliance_pack = compliance_pack
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack:
            self.compliance_pack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack is not None:
            result['CompliancePack'] = self.compliance_pack.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePack') is not None:
            temp_model = GetCompliancePackResponseBodyCompliancePack()
            self.compliance_pack = temp_model.from_map(m['CompliancePack'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCompliancePackReportRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetCompliancePackReportResponseBodyCompliancePackReport(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        compliance_pack_id: str = None,
        report_create_timestamp: int = None,
        report_status: str = None,
        report_url: str = None,
    ):
        self.account_id = account_id
        self.compliance_pack_id = compliance_pack_id
        self.report_create_timestamp = report_create_timestamp
        self.report_status = report_status
        self.report_url = report_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        return self


class GetCompliancePackReportResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_report: GetCompliancePackReportResponseBodyCompliancePackReport = None,
        request_id: str = None,
    ):
        self.compliance_pack_report = compliance_pack_report
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack_report:
            self.compliance_pack_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_report is not None:
            result['CompliancePackReport'] = self.compliance_pack_report.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackReport') is not None:
            temp_model = GetCompliancePackReportResponseBodyCompliancePackReport()
            self.compliance_pack_report = temp_model.from_map(m['CompliancePackReport'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCompliancePackReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCompliancePackReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCompliancePackReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class GetConfigDeliveryChannelResponseBodyDeliveryChannel(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        self.account_id = account_id
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel: GetConfigDeliveryChannelResponseBodyDeliveryChannel = None,
        request_id: str = None,
    ):
        self.delivery_channel = delivery_channel
        self.request_id = request_id

    def validate(self):
        if self.delivery_channel:
            self.delivery_channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel is not None:
            result['DeliveryChannel'] = self.delivery_channel.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannel') is not None:
            temp_model = GetConfigDeliveryChannelResponseBodyDeliveryChannel()
            self.delivery_channel = temp_model.from_map(m['DeliveryChannel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
    ):
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class GetConfigRuleResponseBodyConfigRuleCompliance(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus(TeaModel):
    def __init__(
        self,
        first_activated_timestamp: int = None,
        first_evaluation_started: bool = None,
        last_error_code: str = None,
        last_error_message: str = None,
        last_failed_evaluation_timestamp: int = None,
        last_failed_invocation_timestamp: int = None,
        last_successful_evaluation_timestamp: int = None,
        last_successful_invocation_timestamp: int = None,
    ):
        self.first_activated_timestamp = first_activated_timestamp
        self.first_evaluation_started = first_evaluation_started
        self.last_error_code = last_error_code
        self.last_error_message = last_error_message
        self.last_failed_evaluation_timestamp = last_failed_evaluation_timestamp
        self.last_failed_invocation_timestamp = last_failed_invocation_timestamp
        self.last_successful_evaluation_timestamp = last_successful_evaluation_timestamp
        self.last_successful_invocation_timestamp = last_successful_invocation_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_activated_timestamp is not None:
            result['FirstActivatedTimestamp'] = self.first_activated_timestamp
        if self.first_evaluation_started is not None:
            result['FirstEvaluationStarted'] = self.first_evaluation_started
        if self.last_error_code is not None:
            result['LastErrorCode'] = self.last_error_code
        if self.last_error_message is not None:
            result['LastErrorMessage'] = self.last_error_message
        if self.last_failed_evaluation_timestamp is not None:
            result['LastFailedEvaluationTimestamp'] = self.last_failed_evaluation_timestamp
        if self.last_failed_invocation_timestamp is not None:
            result['LastFailedInvocationTimestamp'] = self.last_failed_invocation_timestamp
        if self.last_successful_evaluation_timestamp is not None:
            result['LastSuccessfulEvaluationTimestamp'] = self.last_successful_evaluation_timestamp
        if self.last_successful_invocation_timestamp is not None:
            result['LastSuccessfulInvocationTimestamp'] = self.last_successful_invocation_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstActivatedTimestamp') is not None:
            self.first_activated_timestamp = m.get('FirstActivatedTimestamp')
        if m.get('FirstEvaluationStarted') is not None:
            self.first_evaluation_started = m.get('FirstEvaluationStarted')
        if m.get('LastErrorCode') is not None:
            self.last_error_code = m.get('LastErrorCode')
        if m.get('LastErrorMessage') is not None:
            self.last_error_message = m.get('LastErrorMessage')
        if m.get('LastFailedEvaluationTimestamp') is not None:
            self.last_failed_evaluation_timestamp = m.get('LastFailedEvaluationTimestamp')
        if m.get('LastFailedInvocationTimestamp') is not None:
            self.last_failed_invocation_timestamp = m.get('LastFailedInvocationTimestamp')
        if m.get('LastSuccessfulEvaluationTimestamp') is not None:
            self.last_successful_evaluation_timestamp = m.get('LastSuccessfulEvaluationTimestamp')
        if m.get('LastSuccessfulInvocationTimestamp') is not None:
            self.last_successful_invocation_timestamp = m.get('LastSuccessfulInvocationTimestamp')
        return self


class GetConfigRuleResponseBodyConfigRuleCreateBy(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        creator_id: str = None,
        creator_name: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.creator_id = creator_id
        self.creator_name = creator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        return self


class GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails(TeaModel):
    def __init__(
        self,
        event_source: str = None,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class GetConfigRuleResponseBodyConfigRuleManagedRule(TeaModel):
    def __init__(
        self,
        compulsory_input_parameter_details: Dict[str, Any] = None,
        description: str = None,
        identifier: str = None,
        labels: List[str] = None,
        managed_rule_name: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        source_details: List[GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails] = None,
    ):
        self.compulsory_input_parameter_details = compulsory_input_parameter_details
        self.description = description
        self.identifier = identifier
        self.labels = labels
        self.managed_rule_name = managed_rule_name
        self.optional_input_parameter_details = optional_input_parameter_details
        self.source_details = source_details

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        if self.description is not None:
            result['Description'] = self.description
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name
        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')
        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        return self


class GetConfigRuleResponseBodyConfigRuleSourceSourceDetails(TeaModel):
    def __init__(
        self,
        event_source: str = None,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        self.event_source = event_source
        self.maximum_execution_frequency = maximum_execution_frequency
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class GetConfigRuleResponseBodyConfigRuleSource(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        owner: str = None,
        source_details: List[GetConfigRuleResponseBodyConfigRuleSourceSourceDetails] = None,
    ):
        self.identifier = identifier
        self.owner = owner
        self.source_details = source_details

    def validate(self):
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.owner is not None:
            result['Owner'] = self.owner
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetConfigRuleResponseBodyConfigRuleSourceSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        return self


class GetConfigRuleResponseBodyConfigRule(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        compliance: GetConfigRuleResponseBodyConfigRuleCompliance = None,
        config_rule_arn: str = None,
        config_rule_evaluation_status: GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_state: str = None,
        config_rule_trigger_types: str = None,
        create_by: GetConfigRuleResponseBodyConfigRuleCreateBy = None,
        create_timestamp: int = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        input_parameters: Dict[str, Any] = None,
        managed_rule: GetConfigRuleResponseBodyConfigRuleManagedRule = None,
        maximum_execution_frequency: str = None,
        modified_timestamp: int = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope: str = None,
        risk_level: int = None,
        source: GetConfigRuleResponseBodyConfigRuleSource = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.account_id = account_id
        self.compliance = compliance
        self.config_rule_arn = config_rule_arn
        self.config_rule_evaluation_status = config_rule_evaluation_status
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_state = config_rule_state
        self.config_rule_trigger_types = config_rule_trigger_types
        self.create_by = create_by
        self.create_timestamp = create_timestamp
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.input_parameters = input_parameters
        self.managed_rule = managed_rule
        self.maximum_execution_frequency = maximum_execution_frequency
        self.modified_timestamp = modified_timestamp
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.source = source
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        if self.compliance:
            self.compliance.validate()
        if self.config_rule_evaluation_status:
            self.config_rule_evaluation_status.validate()
        if self.create_by:
            self.create_by.validate()
        if self.managed_rule:
            self.managed_rule.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.config_rule_evaluation_status is not None:
            result['ConfigRuleEvaluationStatus'] = self.config_rule_evaluation_status.to_map()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Compliance') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleCompliance()
            self.compliance = temp_model.from_map(m['Compliance'])
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ConfigRuleEvaluationStatus') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus()
            self.config_rule_evaluation_status = temp_model.from_map(m['ConfigRuleEvaluationStatus'])
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('CreateBy') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('ManagedRule') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleManagedRule()
            self.managed_rule = temp_model.from_map(m['ManagedRule'])
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Source') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRuleSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class GetConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule: GetConfigRuleResponseBodyConfigRule = None,
        request_id: str = None,
    ):
        self.config_rule = config_rule
        self.request_id = request_id

    def validate(self):
        if self.config_rule:
            self.config_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule is not None:
            result['ConfigRule'] = self.config_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRule') is not None:
            temp_model = GetConfigRuleResponseBodyConfigRule()
            self.config_rule = temp_model.from_map(m['ConfigRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
    ):
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        return self


class GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_compliances: List[GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances] = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_compliances = config_rule_compliances
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count

    def validate(self):
        if self.config_rule_compliances:
            for k in self.config_rule_compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        result['ConfigRuleCompliances'] = []
        if self.config_rule_compliances is not None:
            for k in self.config_rule_compliances:
                result['ConfigRuleCompliances'].append(k.to_map() if k else None)
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        self.config_rule_compliances = []
        if m.get('ConfigRuleCompliances') is not None:
            for k in m.get('ConfigRuleCompliances'):
                temp_model = GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances()
                self.config_rule_compliances.append(temp_model.from_map(k))
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetConfigRuleComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_compliance_result: GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult = None,
        request_id: str = None,
    ):
        self.config_rule_compliance_result = config_rule_compliance_result
        self.request_id = request_id

    def validate(self):
        if self.config_rule_compliance_result:
            self.config_rule_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_compliance_result is not None:
            result['ConfigRuleComplianceResult'] = self.config_rule_compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleComplianceResult') is not None:
            temp_model = GetConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult()
            self.config_rule_compliance_result = temp_model.from_map(m['ConfigRuleComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConfigRuleComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConfigRuleComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConfigRuleComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries(TeaModel):
    def __init__(
        self,
        compliant_count: int = None,
        non_compliant_count: int = None,
        risk_level: int = None,
    ):
        self.compliant_count = compliant_count
        self.non_compliant_count = non_compliant_count
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class GetConfigRuleSummaryByRiskLevelResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_summaries: List[GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries] = None,
        request_id: str = None,
    ):
        self.config_rule_summaries = config_rule_summaries
        self.request_id = request_id

    def validate(self):
        if self.config_rule_summaries:
            for k in self.config_rule_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigRuleSummaries'] = []
        if self.config_rule_summaries is not None:
            for k in self.config_rule_summaries:
                result['ConfigRuleSummaries'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_summaries = []
        if m.get('ConfigRuleSummaries') is not None:
            for k in m.get('ConfigRuleSummaries'):
                temp_model = GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries()
                self.config_rule_summaries.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConfigRuleSummaryByRiskLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConfigRuleSummaryByRiskLevelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConfigRuleSummaryByRiskLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRulesReportRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
    ):
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class GetConfigRulesReportResponseBodyConfigRulesReport(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        report_create_timestamp: int = None,
        report_id: str = None,
        report_status: str = None,
        report_url: str = None,
    ):
        self.account_id = account_id
        self.report_create_timestamp = report_create_timestamp
        self.report_id = report_id
        self.report_status = report_status
        self.report_url = report_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.report_create_timestamp is not None:
            result['ReportCreateTimestamp'] = self.report_create_timestamp
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.report_status is not None:
            result['ReportStatus'] = self.report_status
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ReportCreateTimestamp') is not None:
            self.report_create_timestamp = m.get('ReportCreateTimestamp')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        return self


class GetConfigRulesReportResponseBody(TeaModel):
    def __init__(
        self,
        config_rules_report: GetConfigRulesReportResponseBodyConfigRulesReport = None,
        request_id: str = None,
    ):
        self.config_rules_report = config_rules_report
        self.request_id = request_id

    def validate(self):
        if self.config_rules_report:
            self.config_rules_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rules_report is not None:
            result['ConfigRulesReport'] = self.config_rules_report.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRulesReport') is not None:
            temp_model = GetConfigRulesReportResponseBodyConfigRulesReport()
            self.config_rules_report = temp_model.from_map(m['ConfigRulesReport'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConfigRulesReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConfigRulesReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConfigRulesReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiscoveredResourceRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region = region
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetDiscoveredResourceResponseBodyDiscoveredResourceDetail(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        configuration: str = None,
        region: str = None,
        resource_creation_time: int = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.configuration = configuration
        self.region = region
        self.resource_creation_time = resource_creation_time
        self.resource_deleted = resource_deleted
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetDiscoveredResourceResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_detail: GetDiscoveredResourceResponseBodyDiscoveredResourceDetail = None,
        request_id: str = None,
    ):
        self.discovered_resource_detail = discovered_resource_detail
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_detail:
            self.discovered_resource_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discovered_resource_detail is not None:
            result['DiscoveredResourceDetail'] = self.discovered_resource_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceDetail') is not None:
            temp_model = GetDiscoveredResourceResponseBodyDiscoveredResourceDetail()
            self.discovered_resource_detail = temp_model.from_map(m['DiscoveredResourceDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDiscoveredResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDiscoveredResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDiscoveredResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiscoveredResourceCountsGroupByRegionRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        region: str = None,
        resource_count: int = None,
    ):
        self.group_name = group_name
        self.region = region
        self.resource_count = resource_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        return self


class GetDiscoveredResourceCountsGroupByRegionResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_counts_summary: List[GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary] = None,
        request_id: str = None,
    ):
        self.discovered_resource_counts_summary = discovered_resource_counts_summary
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetDiscoveredResourceCountsGroupByRegionResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDiscoveredResourceCountsGroupByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDiscoveredResourceCountsGroupByRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDiscoveredResourceCountsGroupByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.group_name = group_name
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_counts_summary: List[GetDiscoveredResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary] = None,
        request_id: str = None,
    ):
        self.discovered_resource_counts_summary = discovered_resource_counts_summary
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_counts_summary:
            for k in self.discovered_resource_counts_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiscoveredResourceCountsSummary'] = []
        if self.discovered_resource_counts_summary is not None:
            for k in self.discovered_resource_counts_summary:
                result['DiscoveredResourceCountsSummary'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_counts_summary = []
        if m.get('DiscoveredResourceCountsSummary') is not None:
            for k in m.get('DiscoveredResourceCountsSummary'):
                temp_model = GetDiscoveredResourceCountsGroupByResourceTypeResponseBodyDiscoveredResourceCountsSummary()
                self.discovered_resource_counts_summary.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDiscoveredResourceCountsGroupByResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDiscoveredResourceCountsGroupByResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDiscoveredResourceCountsGroupByResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntegratedServiceStatusRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
    ):
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetIntegratedServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIntegratedServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIntegratedServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetIntegratedServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetManagedRuleRequest(TeaModel):
    def __init__(
        self,
        identifier: str = None,
    ):
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        return self


class GetManagedRuleResponseBodyManagedRuleScope(TeaModel):
    def __init__(
        self,
        compliance_resource_types: List[str] = None,
    ):
        self.compliance_resource_types = compliance_resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_resource_types is not None:
            result['ComplianceResourceTypes'] = self.compliance_resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResourceTypes') is not None:
            self.compliance_resource_types = m.get('ComplianceResourceTypes')
        return self


class GetManagedRuleResponseBodyManagedRuleSourceDetails(TeaModel):
    def __init__(
        self,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        self.maximum_execution_frequency = maximum_execution_frequency
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        return self


class GetManagedRuleResponseBodyManagedRule(TeaModel):
    def __init__(
        self,
        compulsory_input_parameter_details: Dict[str, Any] = None,
        config_rule_name: str = None,
        description: str = None,
        help_urls: str = None,
        identifier: str = None,
        labels: List[str] = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        risk_level: int = None,
        scope: GetManagedRuleResponseBodyManagedRuleScope = None,
        source_details: List[GetManagedRuleResponseBodyManagedRuleSourceDetails] = None,
    ):
        self.compulsory_input_parameter_details = compulsory_input_parameter_details
        self.config_rule_name = config_rule_name
        self.description = description
        self.help_urls = help_urls
        self.identifier = identifier
        self.labels = labels
        self.optional_input_parameter_details = optional_input_parameter_details
        self.risk_level = risk_level
        self.scope = scope
        self.source_details = source_details

    def validate(self):
        if self.scope:
            self.scope.validate()
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.help_urls is not None:
            result['HelpUrls'] = self.help_urls
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.scope is not None:
            result['Scope'] = self.scope.to_map()
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HelpUrls') is not None:
            self.help_urls = m.get('HelpUrls')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Scope') is not None:
            temp_model = GetManagedRuleResponseBodyManagedRuleScope()
            self.scope = temp_model.from_map(m['Scope'])
        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k in m.get('SourceDetails'):
                temp_model = GetManagedRuleResponseBodyManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        return self


class GetManagedRuleResponseBody(TeaModel):
    def __init__(
        self,
        managed_rule: GetManagedRuleResponseBodyManagedRule = None,
        request_id: str = None,
    ):
        self.managed_rule = managed_rule
        self.request_id = request_id

    def validate(self):
        if self.managed_rule:
            self.managed_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRule') is not None:
            temp_model = GetManagedRuleResponseBodyManagedRule()
            self.managed_rule = temp_model.from_map(m['ManagedRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetManagedRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetManagedRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetManagedRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceByConfigRuleRequest(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_id: str = None,
    ):
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetResourceComplianceByConfigRuleResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        compliances: List[GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances] = None,
        total_count: int = None,
    ):
        self.compliances = compliances
        self.total_count = total_count

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetResourceComplianceByConfigRuleResponseBodyComplianceResultCompliances()
                self.compliances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResourceComplianceByConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetResourceComplianceByConfigRuleResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetResourceComplianceByConfigRuleResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceComplianceByConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceComplianceByConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceByConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceByPackRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        return self


class GetResourceComplianceByPackResponseBodyResourceComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.non_compliant_count = non_compliant_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResourceComplianceByPackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_result: GetResourceComplianceByPackResponseBodyResourceComplianceResult = None,
    ):
        self.request_id = request_id
        self.resource_compliance_result = resource_compliance_result

    def validate(self):
        if self.resource_compliance_result:
            self.resource_compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_compliance_result is not None:
            result['ResourceComplianceResult'] = self.resource_compliance_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceComplianceResult') is not None:
            temp_model = GetResourceComplianceByPackResponseBodyResourceComplianceResult()
            self.resource_compliance_result = temp_model.from_map(m['ResourceComplianceResult'])
        return self


class GetResourceComplianceByPackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceComplianceByPackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceByPackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceGroupByRegionRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class GetResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList(TeaModel):
    def __init__(
        self,
        compliances: List[GetResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances] = None,
        region_id: str = None,
    ):
        self.compliances = compliances
        self.region_id = region_id

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultListCompliances()
                self.compliances.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetResourceComplianceGroupByRegionResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_result_list: List[GetResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList] = None,
    ):
        self.compliance_result_list = compliance_result_list

    def validate(self):
        if self.compliance_result_list:
            for k in self.compliance_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplianceResultList'] = []
        if self.compliance_result_list is not None:
            for k in self.compliance_result_list:
                result['ComplianceResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_result_list = []
        if m.get('ComplianceResultList') is not None:
            for k in m.get('ComplianceResultList'):
                temp_model = GetResourceComplianceGroupByRegionResponseBodyComplianceResultComplianceResultList()
                self.compliance_result_list.append(temp_model.from_map(k))
        return self


class GetResourceComplianceGroupByRegionResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetResourceComplianceGroupByRegionResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetResourceComplianceGroupByRegionResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceComplianceGroupByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceComplianceGroupByRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceGroupByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceGroupByResourceTypeRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultListCompliances(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultList(TeaModel):
    def __init__(
        self,
        compliances: List[GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultListCompliances] = None,
        resource_type: str = None,
    ):
        self.compliances = compliances
        self.resource_type = resource_type

    def validate(self):
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliances = []
        if m.get('Compliances') is not None:
            for k in m.get('Compliances'):
                temp_model = GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultListCompliances()
                self.compliances.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResult(TeaModel):
    def __init__(
        self,
        compliance_result_list: List[GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultList] = None,
    ):
        self.compliance_result_list = compliance_result_list

    def validate(self):
        if self.compliance_result_list:
            for k in self.compliance_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplianceResultList'] = []
        if self.compliance_result_list is not None:
            for k in self.compliance_result_list:
                result['ComplianceResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_result_list = []
        if m.get('ComplianceResultList') is not None:
            for k in m.get('ComplianceResultList'):
                temp_model = GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResultComplianceResultList()
                self.compliance_result_list.append(temp_model.from_map(k))
        return self


class GetResourceComplianceGroupByResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        compliance_result: GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResult = None,
        request_id: str = None,
    ):
        self.compliance_result = compliance_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResult') is not None:
            temp_model = GetResourceComplianceGroupByResourceTypeResponseBodyComplianceResult()
            self.compliance_result = temp_model.from_map(m['ComplianceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceComplianceGroupByResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceComplianceGroupByResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceGroupByResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceComplianceTimelineRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        availability_zone: str = None,
        capture_time: int = None,
        configuration: str = None,
        configuration_diff: str = None,
        region: str = None,
        resource_create_time: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.capture_time = capture_time
        self.configuration = configuration
        self.configuration_diff = configuration_diff
        self.region = region
        self.resource_create_time = resource_create_time
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline(TeaModel):
    def __init__(
        self,
        compliance_list: List[GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.compliance_list = compliance_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.compliance_list:
            for k in self.compliance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k in self.compliance_list:
                result['ComplianceList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_list = []
        if m.get('ComplianceList') is not None:
            for k in m.get('ComplianceList'):
                temp_model = GetResourceComplianceTimelineResponseBodyResourceComplianceTimelineComplianceList()
                self.compliance_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetResourceComplianceTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_compliance_timeline: GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline = None,
    ):
        self.request_id = request_id
        self.resource_compliance_timeline = resource_compliance_timeline

    def validate(self):
        if self.resource_compliance_timeline:
            self.resource_compliance_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_compliance_timeline is not None:
            result['ResourceComplianceTimeline'] = self.resource_compliance_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceComplianceTimeline') is not None:
            temp_model = GetResourceComplianceTimelineResponseBodyResourceComplianceTimeline()
            self.resource_compliance_timeline = temp_model.from_map(m['ResourceComplianceTimeline'])
        return self


class GetResourceComplianceTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceComplianceTimelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceComplianceTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceConfigurationTimelineRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        capture_time: str = None,
        configuration_diff: str = None,
        region: str = None,
        relationship: str = None,
        relationship_diff: str = None,
        resource_create_time: str = None,
        resource_event_type: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.capture_time = capture_time
        self.configuration_diff = configuration_diff
        self.region = region
        self.relationship = relationship
        self.relationship_diff = relationship_diff
        self.resource_create_time = resource_create_time
        self.resource_event_type = resource_event_type
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.configuration_diff is not None:
            result['ConfigurationDiff'] = self.configuration_diff
        if self.region is not None:
            result['Region'] = self.region
        if self.relationship is not None:
            result['Relationship'] = self.relationship
        if self.relationship_diff is not None:
            result['RelationshipDiff'] = self.relationship_diff
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.resource_event_type is not None:
            result['ResourceEventType'] = self.resource_event_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ConfigurationDiff') is not None:
            self.configuration_diff = m.get('ConfigurationDiff')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Relationship') is not None:
            self.relationship = m.get('Relationship')
        if m.get('RelationshipDiff') is not None:
            self.relationship_diff = m.get('RelationshipDiff')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('ResourceEventType') is not None:
            self.resource_event_type = m.get('ResourceEventType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline(TeaModel):
    def __init__(
        self,
        configuration_list: List[GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.configuration_list = configuration_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.configuration_list:
            for k in self.configuration_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigurationList'] = []
        if self.configuration_list is not None:
            for k in self.configuration_list:
                result['ConfigurationList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration_list = []
        if m.get('ConfigurationList') is not None:
            for k in m.get('ConfigurationList'):
                temp_model = GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimelineConfigurationList()
                self.configuration_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetResourceConfigurationTimelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_configuration_timeline: GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline = None,
    ):
        self.request_id = request_id
        self.resource_configuration_timeline = resource_configuration_timeline

    def validate(self):
        if self.resource_configuration_timeline:
            self.resource_configuration_timeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_configuration_timeline is not None:
            result['ResourceConfigurationTimeline'] = self.resource_configuration_timeline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceConfigurationTimeline') is not None:
            temp_model = GetResourceConfigurationTimelineResponseBodyResourceConfigurationTimeline()
            self.resource_configuration_timeline = temp_model.from_map(m['ResourceConfigurationTimeline'])
        return self


class GetResourceConfigurationTimelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceConfigurationTimelineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceConfigurationTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IgnoreAggregateEvaluationResultsRequestResources(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region = region
        self.resource_account_id = resource_account_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class IgnoreAggregateEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        ignore_date: str = None,
        reason: str = None,
        resources: List[IgnoreAggregateEvaluationResultsRequestResources] = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id
        self.ignore_date = ignore_date
        self.reason = reason
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.reason is not None:
            result['Reason'] = self.reason
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = IgnoreAggregateEvaluationResultsRequestResources()
                self.resources.append(temp_model.from_map(k))
        return self


class IgnoreAggregateEvaluationResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        ignore_date: str = None,
        reason: str = None,
        resources_shrink: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id
        self.ignore_date = ignore_date
        self.reason = reason
        self.resources_shrink = resources_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.resources_shrink is not None:
            result['Resources'] = self.resources_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')
        return self


class IgnoreAggregateEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IgnoreAggregateEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IgnoreAggregateEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IgnoreAggregateEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IgnoreEvaluationResultsRequestResources(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region = region
        self.resource_account_id = resource_account_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class IgnoreEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        ignore_date: str = None,
        reason: str = None,
        resources: List[IgnoreEvaluationResultsRequestResources] = None,
    ):
        self.config_rule_id = config_rule_id
        self.ignore_date = ignore_date
        self.reason = reason
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.reason is not None:
            result['Reason'] = self.reason
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = IgnoreEvaluationResultsRequestResources()
                self.resources.append(temp_model.from_map(k))
        return self


class IgnoreEvaluationResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        ignore_date: str = None,
        reason: str = None,
        resources_shrink: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.ignore_date = ignore_date
        self.reason = reason
        self.resources_shrink = resources_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.resources_shrink is not None:
            result['Resources'] = self.resources_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')
        return self


class IgnoreEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IgnoreEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IgnoreEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IgnoreEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        create_timestamp: int = None,
        description: str = None,
        risk_level: int = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.create_timestamp = create_timestamp
        self.description = description
        self.risk_level = risk_level
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAggregateCompliancePacksResponseBodyCompliancePacksResult(TeaModel):
    def __init__(
        self,
        compliance_packs: List[ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.compliance_packs = compliance_packs
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.compliance_packs:
            for k in self.compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CompliancePacks'] = []
        if self.compliance_packs is not None:
            for k in self.compliance_packs:
                result['CompliancePacks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_packs = []
        if m.get('CompliancePacks') is not None:
            for k in m.get('CompliancePacks'):
                temp_model = ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks()
                self.compliance_packs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAggregateCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        compliance_packs_result: ListAggregateCompliancePacksResponseBodyCompliancePacksResult = None,
        request_id: str = None,
    ):
        self.compliance_packs_result = compliance_packs_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_packs_result:
            self.compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_packs_result is not None:
            result['CompliancePacksResult'] = self.compliance_packs_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePacksResult') is not None:
            temp_model = ListAggregateCompliancePacksResponseBodyCompliancePacksResult()
            self.compliance_packs_result = temp_model.from_map(m['CompliancePacksResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregateCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregateCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregateCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateConfigDeliveryChannelsRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        delivery_channel_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.delivery_channel_ids = delivery_channel_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.delivery_channel_ids is not None:
            result['DeliveryChannelIds'] = self.delivery_channel_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('DeliveryChannelIds') is not None:
            self.delivery_channel_ids = m.get('DeliveryChannelIds')
        return self


class ListAggregateConfigDeliveryChannelsResponseBodyDeliveryChannels(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAggregateConfigDeliveryChannelsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channels: List[ListAggregateConfigDeliveryChannelsResponseBodyDeliveryChannels] = None,
        request_id: str = None,
    ):
        self.delivery_channels = delivery_channels
        self.request_id = request_id

    def validate(self):
        if self.delivery_channels:
            for k in self.delivery_channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeliveryChannels'] = []
        if self.delivery_channels is not None:
            for k in self.delivery_channels:
                result['DeliveryChannels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_channels = []
        if m.get('DeliveryChannels') is not None:
            for k in m.get('DeliveryChannels'):
                temp_model = ListAggregateConfigDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregateConfigDeliveryChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregateConfigDeliveryChannelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregateConfigDeliveryChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateConfigRuleEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        compliance_type: str = None,
        config_rule_id: str = None,
        max_results: int = None,
        next_token: str = None,
        regions: str = None,
        resource_group_ids: str = None,
        resource_owner_id: int = None,
        resource_types: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id
        self.max_results = max_results
        self.next_token = next_token
        self.regions = regions
        self.resource_group_ids = resource_group_ids
        self.resource_owner_id = resource_owner_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_arn: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        ignore_date: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_arn = config_rule_arn
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.ignore_date = ignore_date
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        evaluation_result_qualifier: ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
        ordering_timestamp: int = None,
    ):
        self.evaluation_result_qualifier = evaluation_result_qualifier
        self.ordering_timestamp = ordering_timestamp

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        annotation: str = None,
        compliance_type: str = None,
        config_rule_invoked_timestamp: int = None,
        evaluation_result_identifier: ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        invoking_event_message_type: str = None,
        remediation_enabled: bool = None,
        result_recorded_timestamp: int = None,
        risk_level: int = None,
    ):
        self.annotation = annotation
        self.compliance_type = compliance_type
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.evaluation_result_identifier = evaluation_result_identifier
        self.invoking_event_message_type = invoking_event_message_type
        self.remediation_enabled = remediation_enabled
        self.result_recorded_timestamp = result_recorded_timestamp
        self.risk_level = risk_level

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        evaluation_result_list: List[ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.evaluation_result_list = evaluation_result_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListAggregateConfigRuleEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        evaluation_results: ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResults = None,
        request_id: str = None,
    ):
        self.evaluation_results = evaluation_results
        self.request_id = request_id

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResults') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregateConfigRuleEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregateConfigRuleEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregateConfigRuleEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateConfigRulesRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_type: str = None,
        config_rule_name: str = None,
        config_rule_state: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        risk_level: int = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_type = compliance_type
        self.config_rule_name = config_rule_name
        self.config_rule_state = config_rule_state
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCompliance(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        self.compliance_type = compliance_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        aggregator_name: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        creator_id: str = None,
        creator_name: str = None,
        creator_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.creator_type = creator_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        return self


class ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleList(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        automation_type: str = None,
        compliance: ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCompliance = None,
        config_rule_arn: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_state: str = None,
        create_by: ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy = None,
        description: str = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tags: List[ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListTags] = None,
    ):
        self.account_id = account_id
        self.automation_type = automation_type
        self.compliance = compliance
        self.config_rule_arn = config_rule_arn
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_state = config_rule_state
        self.create_by = create_by
        self.description = description
        self.risk_level = risk_level
        self.source_identifier = source_identifier
        self.source_owner = source_owner
        self.tags = tags

    def validate(self):
        if self.compliance:
            self.compliance.validate()
        if self.create_by:
            self.create_by.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.automation_type is not None:
            result['AutomationType'] = self.automation_type
        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier
        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AutomationType') is not None:
            self.automation_type = m.get('AutomationType')
        if m.get('Compliance') is not None:
            temp_model = ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCompliance()
            self.compliance = temp_model.from_map(m['Compliance'])
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')
        if m.get('CreateBy') is not None:
            temp_model = ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListCreateBy()
            self.create_by = temp_model.from_map(m['CreateBy'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')
        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleListTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListAggregateConfigRulesResponseBodyConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_list: List[ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.config_rule_list = config_rule_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.config_rule_list:
            for k in self.config_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigRuleList'] = []
        if self.config_rule_list is not None:
            for k in self.config_rule_list:
                result['ConfigRuleList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_list = []
        if m.get('ConfigRuleList') is not None:
            for k in m.get('ConfigRuleList'):
                temp_model = ListAggregateConfigRulesResponseBodyConfigRulesConfigRuleList()
                self.config_rule_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAggregateConfigRulesResponseBody(TeaModel):
    def __init__(
        self,
        config_rules: ListAggregateConfigRulesResponseBodyConfigRules = None,
        request_id: str = None,
    ):
        self.config_rules = config_rules
        self.request_id = request_id

    def validate(self):
        if self.config_rules:
            self.config_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rules is not None:
            result['ConfigRules'] = self.config_rules.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRules') is not None:
            temp_model = ListAggregateConfigRulesResponseBodyConfigRules()
            self.config_rules = temp_model.from_map(m['ConfigRules'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregateConfigRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregateConfigRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregateConfigRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateDiscoveredResourcesRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        max_results: int = None,
        next_token: str = None,
        regions: str = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_types: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.max_results = max_results
        self.next_token = next_token
        self.regions = regions
        self.resource_deleted = resource_deleted
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class ListAggregateDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        region: str = None,
        resource_creation_time: int = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
        version: int = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.region = region
        self.resource_creation_time = resource_creation_time
        self.resource_deleted = resource_deleted
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_owner_id = resource_owner_id
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.tags = tags
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAggregateDiscoveredResourcesResponseBodyDiscoveredResourceProfiles(TeaModel):
    def __init__(
        self,
        discovered_resource_profile_list: List[ListAggregateDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.discovered_resource_profile_list = discovered_resource_profile_list
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.discovered_resource_profile_list:
            for k in self.discovered_resource_profile_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiscoveredResourceProfileList'] = []
        if self.discovered_resource_profile_list is not None:
            for k in self.discovered_resource_profile_list:
                result['DiscoveredResourceProfileList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_profile_list = []
        if m.get('DiscoveredResourceProfileList') is not None:
            for k in m.get('DiscoveredResourceProfileList'):
                temp_model = ListAggregateDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList()
                self.discovered_resource_profile_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAggregateDiscoveredResourcesResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_profiles: ListAggregateDiscoveredResourcesResponseBodyDiscoveredResourceProfiles = None,
        request_id: str = None,
    ):
        self.discovered_resource_profiles = discovered_resource_profiles
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_profiles:
            self.discovered_resource_profiles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discovered_resource_profiles is not None:
            result['DiscoveredResourceProfiles'] = self.discovered_resource_profiles.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceProfiles') is not None:
            temp_model = ListAggregateDiscoveredResourcesResponseBodyDiscoveredResourceProfiles()
            self.discovered_resource_profiles = temp_model.from_map(m['DiscoveredResourceProfiles'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregateDiscoveredResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregateDiscoveredResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregateDiscoveredResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateRemediationsRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_ids: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class ListAggregateRemediationsResponseBodyRemediations(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        config_rule_id: str = None,
        invoke_type: str = None,
        last_successful_invocation_id: str = None,
        last_successful_invocation_time: int = None,
        last_successful_invocation_type: str = None,
        remediaiton_origin_params: str = None,
        remediation_id: str = None,
        remediation_source_type: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
    ):
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id
        self.invoke_type = invoke_type
        self.last_successful_invocation_id = last_successful_invocation_id
        self.last_successful_invocation_time = last_successful_invocation_time
        self.last_successful_invocation_type = last_successful_invocation_type
        self.remediaiton_origin_params = remediaiton_origin_params
        self.remediation_id = remediation_id
        self.remediation_source_type = remediation_source_type
        self.remediation_template_id = remediation_template_id
        self.remediation_type = remediation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.last_successful_invocation_id is not None:
            result['LastSuccessfulInvocationId'] = self.last_successful_invocation_id
        if self.last_successful_invocation_time is not None:
            result['LastSuccessfulInvocationTime'] = self.last_successful_invocation_time
        if self.last_successful_invocation_type is not None:
            result['LastSuccessfulInvocationType'] = self.last_successful_invocation_type
        if self.remediaiton_origin_params is not None:
            result['RemediaitonOriginParams'] = self.remediaiton_origin_params
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.remediation_source_type is not None:
            result['RemediationSourceType'] = self.remediation_source_type
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('LastSuccessfulInvocationId') is not None:
            self.last_successful_invocation_id = m.get('LastSuccessfulInvocationId')
        if m.get('LastSuccessfulInvocationTime') is not None:
            self.last_successful_invocation_time = m.get('LastSuccessfulInvocationTime')
        if m.get('LastSuccessfulInvocationType') is not None:
            self.last_successful_invocation_type = m.get('LastSuccessfulInvocationType')
        if m.get('RemediaitonOriginParams') is not None:
            self.remediaiton_origin_params = m.get('RemediaitonOriginParams')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RemediationSourceType') is not None:
            self.remediation_source_type = m.get('RemediationSourceType')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        return self


class ListAggregateRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        remediations: List[ListAggregateRemediationsResponseBodyRemediations] = None,
        request_id: str = None,
    ):
        self.remediations = remediations
        self.request_id = request_id

    def validate(self):
        if self.remediations:
            for k in self.remediations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Remediations'] = []
        if self.remediations is not None:
            for k in self.remediations:
                result['Remediations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediations = []
        if m.get('Remediations') is not None:
            for k in m.get('Remediations'):
                temp_model = ListAggregateRemediationsResponseBodyRemediations()
                self.remediations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregateRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregateRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregateRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregateResourceEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_type = compliance_type
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        config_rule_arn: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        ignore_date: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.config_rule_arn = config_rule_arn
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.ignore_date = ignore_date
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        evaluation_result_qualifier: ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
        ordering_timestamp: int = None,
    ):
        self.evaluation_result_qualifier = evaluation_result_qualifier
        self.ordering_timestamp = ordering_timestamp

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        annotation: str = None,
        compliance_type: str = None,
        config_rule_invoked_timestamp: int = None,
        evaluation_result_identifier: ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        invoking_event_message_type: str = None,
        remediation_enabled: bool = None,
        result_recorded_timestamp: int = None,
        risk_level: int = None,
    ):
        self.annotation = annotation
        self.compliance_type = compliance_type
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.evaluation_result_identifier = evaluation_result_identifier
        self.invoking_event_message_type = invoking_event_message_type
        self.remediation_enabled = remediation_enabled
        self.result_recorded_timestamp = result_recorded_timestamp
        self.risk_level = risk_level

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListAggregateResourceEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        evaluation_result_list: List[ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.evaluation_result_list = evaluation_result_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListAggregateResourceEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        evaluation_results: ListAggregateResourceEvaluationResultsResponseBodyEvaluationResults = None,
        request_id: str = None,
    ):
        self.evaluation_results = evaluation_results
        self.request_id = request_id

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResults') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregateResourceEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregateResourceEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregateResourceEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAggregatorsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListAggregatorsResponseBodyAggregatorsResultAggregators(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_account_count: int = None,
        aggregator_create_timestamp: int = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        aggregator_status: int = None,
        aggregator_type: str = None,
        description: str = None,
    ):
        self.account_id = account_id
        self.aggregator_account_count = aggregator_account_count
        self.aggregator_create_timestamp = aggregator_create_timestamp
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.aggregator_status = aggregator_status
        self.aggregator_type = aggregator_type
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.aggregator_account_count is not None:
            result['AggregatorAccountCount'] = self.aggregator_account_count
        if self.aggregator_create_timestamp is not None:
            result['AggregatorCreateTimestamp'] = self.aggregator_create_timestamp
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.aggregator_status is not None:
            result['AggregatorStatus'] = self.aggregator_status
        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AggregatorAccountCount') is not None:
            self.aggregator_account_count = m.get('AggregatorAccountCount')
        if m.get('AggregatorCreateTimestamp') is not None:
            self.aggregator_create_timestamp = m.get('AggregatorCreateTimestamp')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('AggregatorStatus') is not None:
            self.aggregator_status = m.get('AggregatorStatus')
        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ListAggregatorsResponseBodyAggregatorsResult(TeaModel):
    def __init__(
        self,
        aggregators: List[ListAggregatorsResponseBodyAggregatorsResultAggregators] = None,
        next_token: str = None,
    ):
        self.aggregators = aggregators
        self.next_token = next_token

    def validate(self):
        if self.aggregators:
            for k in self.aggregators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregators'] = []
        if self.aggregators is not None:
            for k in self.aggregators:
                result['Aggregators'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregators = []
        if m.get('Aggregators') is not None:
            for k in m.get('Aggregators'):
                temp_model = ListAggregatorsResponseBodyAggregatorsResultAggregators()
                self.aggregators.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListAggregatorsResponseBody(TeaModel):
    def __init__(
        self,
        aggregators_result: ListAggregatorsResponseBodyAggregatorsResult = None,
        request_id: str = None,
    ):
        self.aggregators_result = aggregators_result
        self.request_id = request_id

    def validate(self):
        if self.aggregators_result:
            self.aggregators_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators_result is not None:
            result['AggregatorsResult'] = self.aggregators_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorsResult') is not None:
            temp_model = ListAggregatorsResponseBodyAggregatorsResult()
            self.aggregators_result = temp_model.from_map(m['AggregatorsResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAggregatorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAggregatorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAggregatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCompliancePackTemplatesRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.compliance_pack_template_id = compliance_pack_template_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
        required: bool = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_parameters: List[ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters] = None,
        control_description: str = None,
        control_id: str = None,
        default_enable: bool = None,
        description: str = None,
        managed_rule_identifier: str = None,
        managed_rule_name: str = None,
        risk_level: int = None,
    ):
        self.config_rule_parameters = config_rule_parameters
        self.control_description = control_description
        self.control_id = control_id
        self.default_enable = default_enable
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.managed_rule_name = managed_rule_name
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.control_description is not None:
            result['ControlDescription'] = self.control_description
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.default_enable is not None:
            result['DefaultEnable'] = self.default_enable
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('ControlDescription') is not None:
            self.control_description = m.get('ControlDescription')
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('DefaultEnable') is not None:
            self.default_enable = m.get('DefaultEnable')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates(TeaModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        compliance_pack_template_name: str = None,
        config_rules: List[ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules] = None,
        description: str = None,
        labels: str = None,
        last_update: int = None,
        risk_level: int = None,
    ):
        self.compliance_pack_template_id = compliance_pack_template_id
        self.compliance_pack_template_name = compliance_pack_template_name
        self.config_rules = config_rules
        self.description = description
        self.labels = labels
        self.last_update = last_update
        self.risk_level = risk_level

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.compliance_pack_template_name is not None:
            result['CompliancePackTemplateName'] = self.compliance_pack_template_name
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.last_update is not None:
            result['LastUpdate'] = self.last_update
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CompliancePackTemplateName') is not None:
            self.compliance_pack_template_name = m.get('CompliancePackTemplateName')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('LastUpdate') is not None:
            self.last_update = m.get('LastUpdate')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult(TeaModel):
    def __init__(
        self,
        compliance_pack_templates: List[ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.compliance_pack_templates = compliance_pack_templates
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.compliance_pack_templates:
            for k in self.compliance_pack_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CompliancePackTemplates'] = []
        if self.compliance_pack_templates is not None:
            for k in self.compliance_pack_templates:
                result['CompliancePackTemplates'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_pack_templates = []
        if m.get('CompliancePackTemplates') is not None:
            for k in m.get('CompliancePackTemplates'):
                temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates()
                self.compliance_pack_templates.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCompliancePackTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_templates_result: ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult = None,
        request_id: str = None,
    ):
        self.compliance_pack_templates_result = compliance_pack_templates_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack_templates_result:
            self.compliance_pack_templates_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_templates_result is not None:
            result['CompliancePackTemplatesResult'] = self.compliance_pack_templates_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplatesResult') is not None:
            temp_model = ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult()
            self.compliance_pack_templates_result = temp_model.from_map(m['CompliancePackTemplatesResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCompliancePackTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCompliancePackTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCompliancePackTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCompliancePacksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCompliancePacksResponseBodyCompliancePacksResultCompliancePacks(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        create_timestamp: int = None,
        description: str = None,
        risk_level: int = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.compliance_pack_template_id = compliance_pack_template_id
        self.create_timestamp = create_timestamp
        self.description = description
        self.risk_level = risk_level
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListCompliancePacksResponseBodyCompliancePacksResult(TeaModel):
    def __init__(
        self,
        compliance_packs: List[ListCompliancePacksResponseBodyCompliancePacksResultCompliancePacks] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.compliance_packs = compliance_packs
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.compliance_packs:
            for k in self.compliance_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CompliancePacks'] = []
        if self.compliance_packs is not None:
            for k in self.compliance_packs:
                result['CompliancePacks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_packs = []
        if m.get('CompliancePacks') is not None:
            for k in m.get('CompliancePacks'):
                temp_model = ListCompliancePacksResponseBodyCompliancePacksResultCompliancePacks()
                self.compliance_packs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCompliancePacksResponseBody(TeaModel):
    def __init__(
        self,
        compliance_packs_result: ListCompliancePacksResponseBodyCompliancePacksResult = None,
        request_id: str = None,
    ):
        self.compliance_packs_result = compliance_packs_result
        self.request_id = request_id

    def validate(self):
        if self.compliance_packs_result:
            self.compliance_packs_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_packs_result is not None:
            result['CompliancePacksResult'] = self.compliance_packs_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePacksResult') is not None:
            temp_model = ListCompliancePacksResponseBodyCompliancePacksResult()
            self.compliance_packs_result = temp_model.from_map(m['CompliancePacksResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCompliancePacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCompliancePacksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCompliancePacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigDeliveryChannelsRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_ids: str = None,
    ):
        self.delivery_channel_ids = delivery_channel_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_ids is not None:
            result['DeliveryChannelIds'] = self.delivery_channel_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelIds') is not None:
            self.delivery_channel_ids = m.get('DeliveryChannelIds')
        return self


class ListConfigDeliveryChannelsResponseBodyDeliveryChannels(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        self.account_id = account_id
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListConfigDeliveryChannelsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channels: List[ListConfigDeliveryChannelsResponseBodyDeliveryChannels] = None,
        request_id: str = None,
    ):
        self.delivery_channels = delivery_channels
        self.request_id = request_id

    def validate(self):
        if self.delivery_channels:
            for k in self.delivery_channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeliveryChannels'] = []
        if self.delivery_channels is not None:
            for k in self.delivery_channels:
                result['DeliveryChannels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_channels = []
        if m.get('DeliveryChannels') is not None:
            for k in m.get('DeliveryChannels'):
                temp_model = ListConfigDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConfigDeliveryChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConfigDeliveryChannelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConfigDeliveryChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigRuleEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        compliance_type: str = None,
        config_rule_id: str = None,
        max_results: int = None,
        next_token: str = None,
        regions: str = None,
        resource_group_ids: str = None,
        resource_types: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.compliance_type = compliance_type
        self.config_rule_id = config_rule_id
        self.max_results = max_results
        self.next_token = next_token
        self.regions = regions
        self.resource_group_ids = resource_group_ids
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_arn: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        ignore_date: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_arn = config_rule_arn
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.ignore_date = ignore_date
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        evaluation_result_qualifier: ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
        ordering_timestamp: int = None,
    ):
        self.evaluation_result_qualifier = evaluation_result_qualifier
        self.ordering_timestamp = ordering_timestamp

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        annotation: str = None,
        compliance_type: str = None,
        config_rule_invoked_timestamp: int = None,
        evaluation_result_identifier: ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        invoking_event_message_type: str = None,
        remediation_enabled: bool = None,
        result_recorded_timestamp: int = None,
        risk_level: int = None,
    ):
        self.annotation = annotation
        self.compliance_type = compliance_type
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.evaluation_result_identifier = evaluation_result_identifier
        self.invoking_event_message_type = invoking_event_message_type
        self.remediation_enabled = remediation_enabled
        self.result_recorded_timestamp = result_recorded_timestamp
        self.risk_level = risk_level

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListConfigRuleEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        evaluation_result_list: List[ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.evaluation_result_list = evaluation_result_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListConfigRuleEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        evaluation_results: ListConfigRuleEvaluationResultsResponseBodyEvaluationResults = None,
        request_id: str = None,
    ):
        self.evaluation_results = evaluation_results
        self.request_id = request_id

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResults') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConfigRuleEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConfigRuleEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConfigRuleEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiscoveredResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        regions: str = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_types: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.regions = regions
        self.resource_deleted = resource_deleted
        self.resource_id = resource_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        availability_zone: str = None,
        region: str = None,
        resource_creation_time: int = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_status: str = None,
        resource_type: str = None,
        tags: str = None,
        version: int = None,
    ):
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.region = region
        self.resource_creation_time = resource_creation_time
        self.resource_deleted = resource_deleted
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.tags = tags
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_creation_time is not None:
            result['ResourceCreationTime'] = self.resource_creation_time
        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreationTime') is not None:
            self.resource_creation_time = m.get('ResourceCreationTime')
        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles(TeaModel):
    def __init__(
        self,
        discovered_resource_profile_list: List[ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.discovered_resource_profile_list = discovered_resource_profile_list
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.discovered_resource_profile_list:
            for k in self.discovered_resource_profile_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiscoveredResourceProfileList'] = []
        if self.discovered_resource_profile_list is not None:
            for k in self.discovered_resource_profile_list:
                result['DiscoveredResourceProfileList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.discovered_resource_profile_list = []
        if m.get('DiscoveredResourceProfileList') is not None:
            for k in m.get('DiscoveredResourceProfileList'):
                temp_model = ListDiscoveredResourcesResponseBodyDiscoveredResourceProfilesDiscoveredResourceProfileList()
                self.discovered_resource_profile_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDiscoveredResourcesResponseBody(TeaModel):
    def __init__(
        self,
        discovered_resource_profiles: ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles = None,
        request_id: str = None,
    ):
        self.discovered_resource_profiles = discovered_resource_profiles
        self.request_id = request_id

    def validate(self):
        if self.discovered_resource_profiles:
            self.discovered_resource_profiles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discovered_resource_profiles is not None:
            result['DiscoveredResourceProfiles'] = self.discovered_resource_profiles.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredResourceProfiles') is not None:
            temp_model = ListDiscoveredResourcesResponseBodyDiscoveredResourceProfiles()
            self.discovered_resource_profiles = temp_model.from_map(m['DiscoveredResourceProfiles'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDiscoveredResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDiscoveredResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDiscoveredResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListManagedRulesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        risk_level: int = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListManagedRulesResponseBodyManagedRulesManagedRuleList(TeaModel):
    def __init__(
        self,
        config_rule_name: str = None,
        description: str = None,
        help_urls: str = None,
        identifier: str = None,
        labels: List[str] = None,
        risk_level: int = None,
    ):
        self.config_rule_name = config_rule_name
        self.description = description
        self.help_urls = help_urls
        self.identifier = identifier
        self.labels = labels
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.help_urls is not None:
            result['HelpUrls'] = self.help_urls
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HelpUrls') is not None:
            self.help_urls = m.get('HelpUrls')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListManagedRulesResponseBodyManagedRules(TeaModel):
    def __init__(
        self,
        managed_rule_list: List[ListManagedRulesResponseBodyManagedRulesManagedRuleList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.managed_rule_list = managed_rule_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.managed_rule_list:
            for k in self.managed_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ManagedRuleList'] = []
        if self.managed_rule_list is not None:
            for k in self.managed_rule_list:
                result['ManagedRuleList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.managed_rule_list = []
        if m.get('ManagedRuleList') is not None:
            for k in m.get('ManagedRuleList'):
                temp_model = ListManagedRulesResponseBodyManagedRulesManagedRuleList()
                self.managed_rule_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListManagedRulesResponseBody(TeaModel):
    def __init__(
        self,
        managed_rules: ListManagedRulesResponseBodyManagedRules = None,
        request_id: str = None,
    ):
        self.managed_rules = managed_rules
        self.request_id = request_id

    def validate(self):
        if self.managed_rules:
            self.managed_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rules is not None:
            result['ManagedRules'] = self.managed_rules.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRules') is not None:
            temp_model = ListManagedRulesResponseBodyManagedRules()
            self.managed_rules = temp_model.from_map(m['ManagedRules'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListManagedRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListManagedRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListManagedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPreManagedRulesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_types: List[str] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class ListPreManagedRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_types_shrink: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.resource_types_shrink = resource_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_types_shrink is not None:
            result['ResourceTypes'] = self.resource_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceTypes') is not None:
            self.resource_types_shrink = m.get('ResourceTypes')
        return self


class ListPreManagedRulesResponseBodyManagedRules(TeaModel):
    def __init__(
        self,
        compulsory_input_parameter_details: Dict[str, Any] = None,
        config_rule_name: str = None,
        description: str = None,
        help_urls: str = None,
        identifier: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        resource_type: str = None,
    ):
        self.compulsory_input_parameter_details = compulsory_input_parameter_details
        self.config_rule_name = config_rule_name
        self.description = description
        self.help_urls = help_urls
        self.identifier = identifier
        self.optional_input_parameter_details = optional_input_parameter_details
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.description is not None:
            result['Description'] = self.description
        if self.help_urls is not None:
            result['HelpUrls'] = self.help_urls
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HelpUrls') is not None:
            self.help_urls = m.get('HelpUrls')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListPreManagedRulesResponseBody(TeaModel):
    def __init__(
        self,
        managed_rules: List[ListPreManagedRulesResponseBodyManagedRules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.managed_rules = managed_rules
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        if self.managed_rules:
            for k in self.managed_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ManagedRules'] = []
        if self.managed_rules is not None:
            for k in self.managed_rules:
                result['ManagedRules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.managed_rules = []
        if m.get('ManagedRules') is not None:
            for k in m.get('ManagedRules'):
                temp_model = ListPreManagedRulesResponseBodyManagedRules()
                self.managed_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPreManagedRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPreManagedRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPreManagedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRemediationTemplatesRequest(TeaModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        remediation_type: str = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.remediation_type = remediation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        return self


class ListRemediationTemplatesResponseBodyRemediationTemplates(TeaModel):
    def __init__(
        self,
        remediation_type: str = None,
        template_definition: str = None,
        template_identifier: str = None,
        template_name: str = None,
    ):
        self.remediation_type = remediation_type
        self.template_definition = template_definition
        self.template_identifier = template_identifier
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.template_definition is not None:
            result['TemplateDefinition'] = self.template_definition
        if self.template_identifier is not None:
            result['TemplateIdentifier'] = self.template_identifier
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('TemplateDefinition') is not None:
            self.template_definition = m.get('TemplateDefinition')
        if m.get('TemplateIdentifier') is not None:
            self.template_identifier = m.get('TemplateIdentifier')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListRemediationTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        remediation_templates: List[ListRemediationTemplatesResponseBodyRemediationTemplates] = None,
        request_id: str = None,
    ):
        self.remediation_templates = remediation_templates
        self.request_id = request_id

    def validate(self):
        if self.remediation_templates:
            for k in self.remediation_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemediationTemplates'] = []
        if self.remediation_templates is not None:
            for k in self.remediation_templates:
                result['RemediationTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediation_templates = []
        if m.get('RemediationTemplates') is not None:
            for k in m.get('RemediationTemplates'):
                temp_model = ListRemediationTemplatesResponseBodyRemediationTemplates()
                self.remediation_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRemediationTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRemediationTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRemediationTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRemediationsRequest(TeaModel):
    def __init__(
        self,
        config_rule_ids: str = None,
    ):
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')
        return self


class ListRemediationsResponseBodyRemediations(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        config_rule_id: str = None,
        invoke_type: str = None,
        last_successful_invocation_id: str = None,
        last_successful_invocation_time: int = None,
        last_successful_invocation_type: str = None,
        remediation_id: str = None,
        remediation_origin_params: str = None,
        remediation_source_type: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
    ):
        self.account_id = account_id
        self.config_rule_id = config_rule_id
        self.invoke_type = invoke_type
        self.last_successful_invocation_id = last_successful_invocation_id
        self.last_successful_invocation_time = last_successful_invocation_time
        self.last_successful_invocation_type = last_successful_invocation_type
        self.remediation_id = remediation_id
        self.remediation_origin_params = remediation_origin_params
        self.remediation_source_type = remediation_source_type
        self.remediation_template_id = remediation_template_id
        self.remediation_type = remediation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.last_successful_invocation_id is not None:
            result['LastSuccessfulInvocationId'] = self.last_successful_invocation_id
        if self.last_successful_invocation_time is not None:
            result['LastSuccessfulInvocationTime'] = self.last_successful_invocation_time
        if self.last_successful_invocation_type is not None:
            result['LastSuccessfulInvocationType'] = self.last_successful_invocation_type
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.remediation_origin_params is not None:
            result['RemediationOriginParams'] = self.remediation_origin_params
        if self.remediation_source_type is not None:
            result['RemediationSourceType'] = self.remediation_source_type
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('LastSuccessfulInvocationId') is not None:
            self.last_successful_invocation_id = m.get('LastSuccessfulInvocationId')
        if m.get('LastSuccessfulInvocationTime') is not None:
            self.last_successful_invocation_time = m.get('LastSuccessfulInvocationTime')
        if m.get('LastSuccessfulInvocationType') is not None:
            self.last_successful_invocation_type = m.get('LastSuccessfulInvocationType')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RemediationOriginParams') is not None:
            self.remediation_origin_params = m.get('RemediationOriginParams')
        if m.get('RemediationSourceType') is not None:
            self.remediation_source_type = m.get('RemediationSourceType')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        return self


class ListRemediationsResponseBody(TeaModel):
    def __init__(
        self,
        remediations: List[ListRemediationsResponseBodyRemediations] = None,
        request_id: str = None,
    ):
        self.remediations = remediations
        self.request_id = request_id

    def validate(self):
        if self.remediations:
            for k in self.remediations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Remediations'] = []
        if self.remediations is not None:
            for k in self.remediations:
                result['Remediations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediations = []
        if m.get('Remediations') is not None:
            for k in m.get('Remediations'):
                temp_model = ListRemediationsResponseBodyRemediations()
                self.remediations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRemediationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRemediationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRemediationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.compliance_type = compliance_type
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(
        self,
        config_rule_arn: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        ignore_date: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.config_rule_arn = config_rule_arn
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.ignore_date = ignore_date
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(
        self,
        evaluation_result_qualifier: ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier = None,
        ordering_timestamp: int = None,
    ):
        self.evaluation_result_qualifier = evaluation_result_qualifier
        self.ordering_timestamp = ordering_timestamp

    def validate(self):
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        if self.ordering_timestamp is not None:
            result['OrderingTimestamp'] = self.ordering_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResultQualifier') is not None:
            temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(m['EvaluationResultQualifier'])
        if m.get('OrderingTimestamp') is not None:
            self.ordering_timestamp = m.get('OrderingTimestamp')
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(
        self,
        annotation: str = None,
        compliance_type: str = None,
        config_rule_invoked_timestamp: int = None,
        evaluation_result_identifier: ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier = None,
        invoking_event_message_type: str = None,
        remediation_enabled: bool = None,
        result_recorded_timestamp: int = None,
        risk_level: int = None,
    ):
        self.annotation = annotation
        self.compliance_type = compliance_type
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp
        self.evaluation_result_identifier = evaluation_result_identifier
        self.invoking_event_message_type = invoking_event_message_type
        self.remediation_enabled = remediation_enabled
        self.result_recorded_timestamp = result_recorded_timestamp
        self.risk_level = risk_level

    def validate(self):
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotation is not None:
            result['Annotation'] = self.annotation
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.config_rule_invoked_timestamp is not None:
            result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        if self.invoking_event_message_type is not None:
            result['InvokingEventMessageType'] = self.invoking_event_message_type
        if self.remediation_enabled is not None:
            result['RemediationEnabled'] = self.remediation_enabled
        if self.result_recorded_timestamp is not None:
            result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('ConfigRuleInvokedTimestamp') is not None:
            self.config_rule_invoked_timestamp = m.get('ConfigRuleInvokedTimestamp')
        if m.get('EvaluationResultIdentifier') is not None:
            temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(m['EvaluationResultIdentifier'])
        if m.get('InvokingEventMessageType') is not None:
            self.invoking_event_message_type = m.get('InvokingEventMessageType')
        if m.get('RemediationEnabled') is not None:
            self.remediation_enabled = m.get('RemediationEnabled')
        if m.get('ResultRecordedTimestamp') is not None:
            self.result_recorded_timestamp = m.get('ResultRecordedTimestamp')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ListResourceEvaluationResultsResponseBodyEvaluationResults(TeaModel):
    def __init__(
        self,
        evaluation_result_list: List[ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.evaluation_result_list = evaluation_result_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_result_list = []
        if m.get('EvaluationResultList') is not None:
            for k in m.get('EvaluationResultList'):
                temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListResourceEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        evaluation_results: ListResourceEvaluationResultsResponseBodyEvaluationResults = None,
        request_id: str = None,
    ):
        self.evaluation_results = evaluation_results
        self.request_id = request_id

    def validate(self):
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationResults') is not None:
            temp_model = ListResourceEvaluationResultsResponseBodyEvaluationResults()
            self.evaluation_results = temp_model.from_map(m['EvaluationResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourceEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevertAggregateEvaluationResultsRequestResources(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region = region
        self.resource_account_id = resource_account_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class RevertAggregateEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        resources: List[RevertAggregateEvaluationResultsRequestResources] = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = RevertAggregateEvaluationResultsRequestResources()
                self.resources.append(temp_model.from_map(k))
        return self


class RevertAggregateEvaluationResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        resources_shrink: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id
        self.resources_shrink = resources_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resources_shrink is not None:
            result['Resources'] = self.resources_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')
        return self


class RevertAggregateEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevertAggregateEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevertAggregateEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevertAggregateEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevertEvaluationResultsRequestResources(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.region = region
        self.resource_account_id = resource_account_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class RevertEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        resources: List[RevertEvaluationResultsRequestResources] = None,
    ):
        self.config_rule_id = config_rule_id
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = RevertEvaluationResultsRequestResources()
                self.resources.append(temp_model.from_map(k))
        return self


class RevertEvaluationResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        resources_shrink: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.resources_shrink = resources_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.resources_shrink is not None:
            result['Resources'] = self.resources_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')
        return self


class RevertEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevertEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevertEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevertEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAggregateConfigRuleEvaluationRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        config_rule_id: str = None,
        revert_evaluation: bool = None,
    ):
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_id = config_rule_id
        self.revert_evaluation = revert_evaluation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.revert_evaluation is not None:
            result['RevertEvaluation'] = self.revert_evaluation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RevertEvaluation') is not None:
            self.revert_evaluation = m.get('RevertEvaluation')
        return self


class StartAggregateConfigRuleEvaluationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StartAggregateConfigRuleEvaluationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAggregateConfigRuleEvaluationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartAggregateConfigRuleEvaluationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAggregateRemediationRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class StartAggregateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAggregateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAggregateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartAggregateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRemediationRequest(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
    ):
        self.config_rule_id = config_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        return self


class StartRemediationResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartRemediationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopConfigurationRecorderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stop_configuration_recorder_result: bool = None,
    ):
        self.request_id = request_id
        self.stop_configuration_recorder_result = stop_configuration_recorder_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stop_configuration_recorder_result is not None:
            result['StopConfigurationRecorderResult'] = self.stop_configuration_recorder_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StopConfigurationRecorderResult') is not None:
            self.stop_configuration_recorder_result = m.get('StopConfigurationRecorderResult')
        return self


class StopConfigurationRecorderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopConfigurationRecorderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopConfigurationRecorderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class UpdateAggregateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        risk_level: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class UpdateAggregateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        config_rules: List[UpdateAggregateCompliancePackRequestConfigRules] = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.config_rules = config_rules
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = UpdateAggregateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateAggregateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        config_rules_shrink: str = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.config_rules_shrink = config_rules_shrink
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateAggregateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAggregateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAggregateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAggregateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregateConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAggregateConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAggregateConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAggregateConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAggregateConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        folder_ids_scope: str = None,
        input_parameters: Dict[str, Any] = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_account_ids_scope = exclude_account_ids_scope
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.folder_ids_scope = folder_ids_scope
        self.input_parameters = input_parameters
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_account_ids_scope is not None:
            result['ExcludeAccountIdsScope'] = self.exclude_account_ids_scope
        if self.exclude_folder_ids_scope is not None:
            result['ExcludeFolderIdsScope'] = self.exclude_folder_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.folder_ids_scope is not None:
            result['FolderIdsScope'] = self.folder_ids_scope
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeAccountIdsScope') is not None:
            self.exclude_account_ids_scope = m.get('ExcludeAccountIdsScope')
        if m.get('ExcludeFolderIdsScope') is not None:
            self.exclude_folder_ids_scope = m.get('ExcludeFolderIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('FolderIdsScope') is not None:
            self.folder_ids_scope = m.get('FolderIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateAggregateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        folder_ids_scope: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.client_token = client_token
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_account_ids_scope = exclude_account_ids_scope
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.folder_ids_scope = folder_ids_scope
        self.input_parameters_shrink = input_parameters_shrink
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_account_ids_scope is not None:
            result['ExcludeAccountIdsScope'] = self.exclude_account_ids_scope
        if self.exclude_folder_ids_scope is not None:
            result['ExcludeFolderIdsScope'] = self.exclude_folder_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.folder_ids_scope is not None:
            result['FolderIdsScope'] = self.folder_ids_scope
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeAccountIdsScope') is not None:
            self.exclude_account_ids_scope = m.get('ExcludeAccountIdsScope')
        if m.get('ExcludeFolderIdsScope') is not None:
            self.exclude_folder_ids_scope = m.get('ExcludeFolderIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('FolderIdsScope') is not None:
            self.folder_ids_scope = m.get('FolderIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateAggregateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAggregateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAggregateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAggregateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregateRemediationRequest(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        invoke_type: str = None,
        params: str = None,
        remediation_id: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
        source_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.invoke_type = invoke_type
        self.params = params
        self.remediation_id = remediation_id
        self.remediation_template_id = remediation_template_id
        self.remediation_type = remediation_type
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.params is not None:
            result['Params'] = self.params
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class UpdateAggregateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        request_id: str = None,
    ):
        self.remediation_id = remediation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAggregateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAggregateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAggregateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAggregatorRequestAggregatorAccounts(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        account_type: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class UpdateAggregatorRequest(TeaModel):
    def __init__(
        self,
        aggregator_accounts: List[UpdateAggregatorRequestAggregatorAccounts] = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.aggregator_accounts = aggregator_accounts
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.client_token = client_token
        self.description = description

    def validate(self):
        if self.aggregator_accounts:
            for k in self.aggregator_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AggregatorAccounts'] = []
        if self.aggregator_accounts is not None:
            for k in self.aggregator_accounts:
                result['AggregatorAccounts'].append(k.to_map() if k else None)
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregator_accounts = []
        if m.get('AggregatorAccounts') is not None:
            for k in m.get('AggregatorAccounts'):
                temp_model = UpdateAggregatorRequestAggregatorAccounts()
                self.aggregator_accounts.append(temp_model.from_map(k))
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateAggregatorShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregator_accounts_shrink: str = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.aggregator_accounts_shrink = aggregator_accounts_shrink
        self.aggregator_id = aggregator_id
        self.aggregator_name = aggregator_name
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_accounts_shrink is not None:
            result['AggregatorAccounts'] = self.aggregator_accounts_shrink
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorAccounts') is not None:
            self.aggregator_accounts_shrink = m.get('AggregatorAccounts')
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateAggregatorResponseBody(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        request_id: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAggregatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAggregatorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAggregatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCompliancePackRequestConfigRulesConfigRuleParameters(TeaModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class UpdateCompliancePackRequestConfigRules(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[UpdateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        risk_level: int = None,
    ):
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_parameters = config_rule_parameters
        self.description = description
        self.managed_rule_identifier = managed_rule_identifier
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for k in self.config_rule_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k in m.get('ConfigRuleParameters'):
                temp_model = UpdateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class UpdateCompliancePackRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        config_rules: List[UpdateCompliancePackRequestConfigRules] = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.config_rules = config_rules
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        if self.config_rules:
            for k in self.config_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k in self.config_rules:
                result['ConfigRules'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k in m.get('ConfigRules'):
                temp_model = UpdateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateCompliancePackShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        config_rules_shrink: str = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        risk_level: int = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.compliance_pack_id = compliance_pack_id
        self.compliance_pack_name = compliance_pack_name
        self.config_rules_shrink = config_rules_shrink
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.risk_level = risk_level
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name
        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')
        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateCompliancePackResponseBody(TeaModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        request_id: str = None,
    ):
        self.compliance_pack_id = compliance_pack_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCompliancePackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCompliancePackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCompliancePackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        self.client_token = client_token
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateConfigDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConfigDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConfigDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConfigDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        input_parameters: Dict[str, Any] = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.input_parameters = input_parameters
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope = resource_types_scope
        self.risk_level = risk_level
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateConfigRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_resource_ids_scope: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
    ):
        self.client_token = client_token
        self.config_rule_id = config_rule_id
        self.config_rule_name = config_rule_name
        self.config_rule_trigger_types = config_rule_trigger_types
        self.description = description
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        self.input_parameters_shrink = input_parameters_shrink
        self.maximum_execution_frequency = maximum_execution_frequency
        self.region_ids_scope = region_ids_scope
        self.resource_group_ids_scope = resource_group_ids_scope
        self.resource_types_scope_shrink = resource_types_scope_shrink
        self.risk_level = risk_level
        self.tag_key_logic_scope = tag_key_logic_scope
        self.tag_key_scope = tag_key_scope
        self.tag_value_scope = tag_value_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name
        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types
        if self.description is not None:
            result['Description'] = self.description
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope
        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope
        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')
        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')
        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')
        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')
        return self


class UpdateConfigRuleResponseBody(TeaModel):
    def __init__(
        self,
        config_rule_id: str = None,
        request_id: str = None,
    ):
        self.config_rule_id = config_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConfigRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConfigRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConfigRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        self.client_token = client_token
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification
        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot
        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        if self.description is not None:
            result['Description'] = self.description
        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification
        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')
        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')
        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')
        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')
        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntegratedServiceStatusRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        status: bool = None,
    ):
        self.service_code = service_code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateIntegratedServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIntegratedServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIntegratedServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateIntegratedServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRemediationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        invoke_type: str = None,
        params: str = None,
        remediation_id: str = None,
        remediation_template_id: str = None,
        remediation_type: str = None,
        source_type: str = None,
    ):
        self.client_token = client_token
        self.invoke_type = invoke_type
        self.params = params
        self.remediation_id = remediation_id
        self.remediation_template_id = remediation_template_id
        self.remediation_type = remediation_type
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type
        if self.params is not None:
            result['Params'] = self.params
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.remediation_template_id is not None:
            result['RemediationTemplateId'] = self.remediation_template_id
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RemediationTemplateId') is not None:
            self.remediation_template_id = m.get('RemediationTemplateId')
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class UpdateRemediationResponseBody(TeaModel):
    def __init__(
        self,
        remediation_id: str = None,
        request_id: str = None,
    ):
        self.remediation_id = remediation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRemediationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRemediationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRemediationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


