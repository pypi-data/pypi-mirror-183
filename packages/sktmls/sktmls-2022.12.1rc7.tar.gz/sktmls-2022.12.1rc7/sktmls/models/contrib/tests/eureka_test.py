from sktmls.apis import MLSProfileAPIClient
from typing import Dict, List, Any
from sktmls import MLSENV, MLSRuntimeENV
from sktmls.utils import LogicConverter
from sktmls.models import MLSModelError


class EurekaModelTest(MLSProfileAPIClient):
    def __init__(
        self,
        profile_id: str,
        model,
        client_id: str = "netcrm",
        apikey: str = "DGHIIVU4PS4FI9ECJJ7QWHKN9OS8OHVGR1S961YC",
        env: str = "stg",
        runtime_env: str = "ye",
        additional_keys: str = None,
    ):
        """
        AutoGluon을 통해 학습한 모델의 테스트를 지원합니다.
        ## Example
        # 기학습 모델 준비
        model_test = EurekaModelTest(
            profile_id='user_profile_smp_result',
            model = kyu_test_model,
            client_id = "netcrm",
            apikey = "DGHIIVU4PS4FI9ECJJ7QWHKN9OS8OHVGR1S961YC",
            env = "stg",
            runtime_env = "ye",
        )
        # prediction & 후처리 테스트 Example
        result = model_test.test_logic(user_id = user_id)
        print(result)
        [{'id': 'prod_id', 'name': 'prod_nm', 'type': 'vas', 'agprod_nme': '5GX 레귤러', 'priority': 'N', 'props': {'class': 'sub', 'fee_prod_id': 'NA00006402', 'score': 0.4414701759815216}}]

        #전처리 결과
        user_profile_dict, preprocessed_features = model_test._preprocess_logic_test(user_id = user_id)
        #예측 결과
        predictions = model_test._ml_prediction_test(preprocessed_features = preprocessed_features)
        #후처리 결과
        result = model_test._postprocess_logic_test(user_profile_dict = user_profile_dict
                                                   , user_id = user_id
                                                   , additional_keys = None
                                                   , predictions = predictions)
        print(result)

        user_profile_dict, preprocessed_features, predictions = model_test._ml_predict(user_id=user_id)
        print(predictions)
        [0.7659122347831726, 0.2340877503156662]
        # 후처리 테스트
        results= model_test._postprocess_logic_test(user_profile_dict = user_profile_dict, user_id = user_id, predictions = predictions)
        print(results)
        [{'id': 'prod_id', 'name': 'prod_nm', 'type': 'vas', 'agprod_nme': '5GX 레귤러', 'priority': 'N', 'props': {'class': 'sub', 'fee_prod_id': 'NA00006402', 'score': 0.4414701759815216}}]
        """
        assert type(env) is str, "테스트 환경 값은 String 이어야 합니다.(stg, dev, prd)"
        assert type(runtime_env) is str, "runtime_env 값은 String 이어야 합니다.(ye, mms etc)"
        assert type(profile_id) is str, "profile_id 값은 String 이어야 합니다.(user_profile_smp_result etc)"
        assert type(client_id) is str, "client_id 값은 String 이어야 합니다.(netcrm etc)"
        assert type(apikey) is str, "apikey 값은 String 이어야 합니다. "
        self.env = env
        self.profile_id = profile_id
        self.model = model
        self.pf_client = MLSProfileAPIClient(
            env=MLSENV.PRD if env == "prd" else MLSENV.STG,
            runtime_env=MLSRuntimeENV.MMS if runtime_env == "mms" else MLSRuntimeENV.YE,
            client_id=client_id,
            apikey=apikey,
        )
        self.additional_keys = additional_keys

    def _preprocess_logic_test(
        self,
        user_id: str,
    ) -> List[Any]:
        assert type(user_id) is str, "테스트하고자 하는 유저 ID 값은 str 이어야 합니다."

        user_profile_dict = self.pf_client.get_user_profile(
            profile_id=self.profile_id,
            user_id=user_id,
            keys=self.model.features,
        )

        # features 순서에 맞게 리스트로 정리
        feature_values = [user_profile_dict[feature_name] for feature_name in self.model.features]
        # Preprocessing
        preprocessed_features = self.model._preprocess(
            x=feature_values,
            additional_keys=self.additional_keys,
            pf_client=self.pf_client,
            dynamodb_client=None,
            graph_client=None,
        )
        return user_profile_dict, preprocessed_features

    def _ml_prediction_test(
        self,
        preprocessed_features,
    ) -> List[Any]:
        """
        AutoGluon을 통해 학습한 모델의 전처리 및 예측 결과를 반환합니다.
        ## Example
        # 학습 및 테스트 데이터 준비
        model_test = MLSModelTest(
            profile_id=profile_id,
            model = model_name,
            client_id = client_id,
            apikey = apikey,
            env = "stg",
            runtime_env = "ye",
        )
        # prediction Example
        user_profile_dict, preprocessed_features, predictions = model_test._ml_predict(user_id=user_id)
        print(predictions)
        [0.7659122347831726, 0.2340877503156662]
        """
        # ML Prediction
        predictions = self.model._ml_predict(preprocessed_x=preprocessed_features)

        return predictions

    def _postprocess_logic_test(
        self, user_profile_dict: Dict[str, Any], user_id: str, additional_keys: str, predictions: Dict[str, Any] = None
    ):
        """
        AutoGluon을 통해 학습한 모델의 후처리 결과를 반환합니다.
        ## 참고 사항
        - `postprocess_logic_func` 함수를 통해 동작하므로 postprocess_logic_func 는 함수여야 합니다.
        ## 후처리 Example
        results= model_test._postprocess_logic_test(user_profile_dict = user_profile_dict, user_id = user_id, predictions = predictions)
        print(results)
        [{'id': 'prod_id', 'name': 'prod_nm', 'type': 'vas', 'agprod_nme': '5GX 레귤러', 'priority': 'N', 'props': {'class': 'sub', 'fee_prod_id': 'NA00006402', 'score': 0.4414701759815216}}]
        """
        assert isinstance(user_profile_dict, dict), "`user_profile_dict`는 dict 타입이어야 합니다."
        assert type(user_id) is str, "테스트하고자 하는 유저 ID 값은 str 이어야 합니다."
        assert type(predictions) is list, "테스트하고자 하는 predictions 값은 list 이어야 합니다."
        data = user_profile_dict
        data["additional_keys"] = self.additional_keys
        data["y"] = predictions
        data["user_id"] = user_id

        postprocessing_user_profile = self.model.postprocessing_user_profile
        if postprocessing_user_profile:
            for user_profile in postprocessing_user_profile:
                user_values = self.pf_client.get_user_profile(
                    profile_id=user_profile, user_id=data["user_id"], keys=postprocessing_user_profile[user_profile]
                )
                assert (
                    None not in user_values.values()
                ), "후처리 시 사용되는 `user profile` 변수의 값은 사용되는 `user profile`에 있어야 합니다."
                data.update(user_values)

        postprocessing_item_profile_preprocessed = self.model._get_var(
            data=data, postprocessing_item_profile=self.model.postprocessing_item_profile
        )

        if postprocessing_item_profile_preprocessed:
            for item_profile in postprocessing_item_profile_preprocessed:
                for item_id, keys in postprocessing_item_profile_preprocessed[item_profile].items():
                    item_values = self.pf_client.get_item_profile(profile_id=item_profile, item_id=item_id, keys=keys)
                    data.update(item_values)
                    assert (
                        None not in user_values.values()
                    ), "후처리 시 사용되는 `item profile` 변수의 값은 사용되는 `item profile`에 있어야 합니다."
        try:
            if self.model.postprocess_byte is not None:
                assert isinstance(self.model.postprocess_logic, bytes), "`postprocess_logic`은 bytes 타입이어야 합니다."
                Handler, Handler_string = LogicConverter(
                    user_defined_bytes=self.model.postprocess_logic
                ).BytesToFunction(name=f"{self.model.model_name}_{self.model.model_version}_Handler")
                assert hasattr(Handler, "__call__") is True, "후처리 로직은 함수이어야 합니다."
                return Handler(data)
        except Exception as e:
            raise MLSModelError(f"GenericLogicModelCustom: 후처리에 실패했습니다. {e}")

    def test_logic(
        self,
        user_id: str,
    ) -> Any:
        """
        AutoGluon을 통해 학습한 모델의 테스트를 지원합니다.
        # prediction & 후처리 테스트 Example
        result = model_test.test_logic(user_id = user_id)
        print(result)
        [{'id': 'prod_id', 'name': 'prod_nm', 'type': 'vas', 'agprod_nme': '5GX 레귤러', 'priority': 'N', 'props': {'class': 'sub', 'fee_prod_id': 'NA00006402', 'score': 0.4414701759815216}}]
        """

        user_profile_dict, preprocessed_features = self._preprocess_logic_test(user_id=user_id)
        predictions = self._ml_prediction_test(preprocessed_features=preprocessed_features)
        return self.model._postprocess(
            x=preprocessed_features + [user_id],
            additional_keys=self.additional_keys,
            y=predictions,
            pf_client=self.pf_client,
            graph_client=None,
            dynamodb_client=None,
        )
