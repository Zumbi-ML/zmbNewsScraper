# -*- coding: UTF-8 -*-

class ZmbLabels:

    class SOURCE:
        def api():
            return "sources"
        def ner():
            return "SOURCE"

    class MEDIA:
        def api():
            return "media"
        def ner():
            return "MEDIA"

    class LAW:
        def api():
            return "laws"
        def ner():
            return "LAW"

    class MOVEMENT:
        def api():
            return "movements"
        def ner():
            return "MOVEMENT"

    class PEOPLE:
        def api():
            return "people"
        def ner():
            return "PER"

    class PRIVATE:
        def api():
            return "private"
        def ner():
            return "ORG"

    class PUBLIC:
        def api():
            return "public"
        def ner():
            return "PUBLIC"

    class WORK:
        def api():
            return "works"
        def ner():
            return "WORK"

    class EDUCATIONAL:
        def api():
            return "educational"
        def ner():
            return "EDUCATIONAL"

    class COUNTRY:
        def api():
            return "countries"
        def ner():
            return "COUNTRY"

    class STATE:
        def api():
            return "states"
        def ner():
            return "STATE"

    class CITY:
        def api():
            return "cities"
        def ner():
            return "CITY"

    class POLICE:
        def api():
            return "polices"
        def ner():
            return "POLICE"

    class ACTION:
        def api():
            return "actions"
        def ner():
            return "ACTION"

    def find_api_label(ner_label):
        if (ner_label == ZmbLabels.SOURCE.ner()):
            return ZmbLabels.SOURCE.api()
        elif (ner_label == ZmbLabels.MEDIA.ner()):
            return ZmbLabels.MEDIA.api()
        elif (ner_label == ZmbLabels.LAW.ner()):
            return ZmbLabels.LAW.api()
        elif (ner_label == ZmbLabels.MOVEMENT.ner()):
            return ZmbLabels.MOVEMENT.api()
        elif (ner_label == ZmbLabels.PEOPLE.ner()):
            return ZmbLabels.PEOPLE.api()
        elif (ner_label == ZmbLabels.PRIVATE.ner()):
            return ZmbLabels.PRIVATE.api()
        elif (ner_label == ZmbLabels.PUBLIC.ner()):
            return ZmbLabels.PUBLIC.api()
        elif (ner_label == ZmbLabels.WORK.ner()):
            return ZmbLabels.WORK.api()
        elif (ner_label == ZmbLabels.EDUCATIONAL.ner()):
            return ZmbLabels.EDUCATIONAL.api()
        elif (ner_label == ZmbLabels.COUNTRY.ner()):
            return ZmbLabels.COUNTRY.api()
        elif (ner_label == ZmbLabels.STATE.ner()):
            return ZmbLabels.STATE.api()
        elif (ner_label == ZmbLabels.CITY.ner()):
            return ZmbLabels.CITY.api()
        elif (ner_label == ZmbLabels.POLICE.ner()):
            return ZmbLabels.POLICE.api()
        elif (ner_label == ZmbLabels.ACTION.ner()):
            return ZmbLabels.ACTION.api()
        return None

    def find_ner_label(api_label):
        if (api_label == ZmbLabels.SOURCE.api()):
            return ZmbLabels.SOURCE.ner()
        elif (api_label == ZmbLabels.MEDIA.api()):
            return ZmbLabels.MEDIA.ner()
        elif (api_label == ZmbLabels.LAW.api()):
            return ZmbLabels.LAW.ner()
        elif (api_label == ZmbLabels.MOVEMENT.api()):
            return ZmbLabels.MOVEMENT.ner()
        elif (api_label == ZmbLabels.PEOPLE.api()):
            return ZmbLabels.PEOPLE.ner()
        elif (api_label == ZmbLabels.PRIVATE.api()):
            return ZmbLabels.PRIVATE.ner()
        elif (api_label == ZmbLabels.PUBLIC.api()):
            return ZmbLabels.PUBLIC.ner()
        elif (api_label == ZmbLabels.WORK.api()):
            return ZmbLabels.WORK.ner()
        elif (api_label == ZmbLabels.EDUCATIONAL.api()):
            return ZmbLabels.EDUCATIONAL.ner()
        elif (api_label == ZmbLabels.COUNTRY.api()):
            return ZmbLabels.COUNTRY.ner()
        elif (api_label == ZmbLabels.STATE.api()):
            return ZmbLabels.STATE.ner()
        elif (api_label == ZmbLabels.CITY.api()):
            return ZmbLabels.CITY.ner()
        elif (api_label == ZmbLabels.POLICE.api()):
            return ZmbLabels.POLICE.ner()
        elif (api_label == ZmbLabels.ACTION.api()):
            return ZmbLabels.ACTION.ner()
        return None

    def convert_into_api_format(entities_map):
        api_entities_map = {}
        for ner_label in entities_map.keys():
            api_label = ZmbLabels.find_api_label(ner_label)
            if (not api_label in api_entities_map.keys()):
                api_entities_map[api_label] = []
            for entity in entities_map[ner_label]:
                api_entities_map[api_label].append(entity)
        return api_entities_map
