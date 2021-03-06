import pytest


class TestVertex:

    @pytest.fixture
    def graph_manager(self):
        from gremlin_crud.manager import GremlinCRUDManager
        return GremlinCRUDManager("ws://127.0.0.1:8182/gremlin")

    def test_create_vertex(self, graph_manager):
        graph_manager.process(
            type="vertex",
            operation_type="create",
            payload={
                "label": "Plant",
                "data": {
                    "common_name": "chrysanths",
                    "scientific_name": "Chrysanthemum"
                }
            })

    def test_updated_vertex(self, graph_manager):
        graph_manager.process(
            type="vertex",
            operation_type="update",
            payload={
                "label": "Plant",
                "data": {
                    "new_field": "im new field data",
                },
                "query": {
                    "scientific_name": "Chrysanthemum"
                }
            })

    def test_read_one_vertex(self, graph_manager):
        vtx = graph_manager.process(
            type="vertex",
            operation_type="read_one",
            payload={
                "label": "Plant",
                "query": {
                    "scientific_name": "Chrysanthemum"
                }
            }
        )

    def test_read_vertex(self, graph_manager):
        vtx = graph_manager.process(
            type="vertex",
            operation_type="read_many",
            payload={
                "label": "Plant",
            }
        )

    def test_delete_vertex(self, graph_manager):
        graph_manager.process(
            type="vertex",
            operation_type="delete",
            payload={
                "label": "Plant"
            }
        )
