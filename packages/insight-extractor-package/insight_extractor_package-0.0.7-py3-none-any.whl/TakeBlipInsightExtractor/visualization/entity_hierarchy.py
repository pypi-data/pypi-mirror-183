import operator
import json
import typing as tp
import plotly.express as px


def create_parent_dict(entity_frequency_dict: dict,
                       entity_cluster_dict: dict) -> dict:
    """Create the dictionaries for entity - cluster name

    Receive one dictionary with the frequency of each entity (entity as key
    and frequency as value) and one dictionary with the cluster id (entity
    as key and cluster id as values). And create two dictionaries:

    * Entities_parent_dictionary: dictionary with the relation of entity
    and cluster name (parent). Entity as key and cluster name as value.

    * Parent_entities_dictionary: dictionary with the relation of cluster
    name(parent) and all entities in the cluster. Cluster name as key and
    list with all entities as value.

    Parameters
    ----------
    entity_frequency_dict: dict
       dictionary entity as key and frequency as value.
    entity_cluster_dict: dict
        dictionary entity as key and cluster id as value.

    Returns
    -------
    dict
        Dictionary with the relation parent - entities
    """
    parent_entity_dict = {}

    num_clusters = max(entity_cluster_dict.values()) + 1

    cluster_name = {}

    for entity, cluster in entity_cluster_dict.items():
        if parent_entity_dict.get(cluster, None):
            cluster_freq = entity_frequency_dict[cluster_name[cluster]]
            parent_entity_dict[cluster].append(entity)
            if entity_frequency_dict[entity] > cluster_freq:
                cluster_name.update({cluster: entity})
        else:
            parent_entity_dict[cluster] = [entity]
            cluster_name[cluster] = entity

    for k in range(num_clusters):
        parent_cluster = cluster_name[k]
        parent_entity_dict[parent_cluster] = parent_entity_dict.pop(k)

    return parent_entity_dict


def add_entities(relation_list: list,
                 parent_entity_dict: dict,
                 filtered_messages_dict: dict,
                 node_messages_examples: int) -> list:
    """Add entities to the relation list

    Create by adding the nodes and leaves of the three. The first value of
    the sub-list is the word to be printed, the second value is the id of
    the node (leaf), the third is the id of the parent node, and last the
    color.

    The first branch is the cluster name, the second is the entity and
    the last is the sample messages.

    Parameters
    ----------
    relation_list: list
        a list with the representation root of the tree.
    parent_entity_dict: dict
        dictionary with the entity-cluster relation.
    filtered_messages_dict: dict
        dictionary with the entity-message relation.
    node_messages_examples: int
        maximum of leaves in each branch.

    Returns
    -------
    list
        a list with the representation of the tree.
    """
    ind_cluster = len(parent_entity_dict)
    ind_entities = ind_cluster + 1
    ind_message = ind_cluster + sum([len(value) for value in
                                     list(parent_entity_dict.values())]) + 1
    cluster_list = sorted_cluster(parent_entity_dict, filtered_messages_dict)
    for k in range(ind_cluster):
        cluster = cluster_list[k]
        relation_list += [[k + 1, cluster[0], 0, 1, 'white']]
        for i in range(len(cluster[1])):
            value = cluster[1][i]
            freq_others = sum([freq for _, freq in
                               cluster[2][i][node_messages_examples:]])
            freq_show = sum([freq for _, freq in
                             cluster[2][i][:node_messages_examples]])
            relation_list += [[ind_entities, value, k + 1,
                               freq_others + freq_show, 'white']]
            if freq_others < 0.6 * (freq_show + freq_others):
                for msg, freq in cluster[2][i][:node_messages_examples]:
                    relation_list += [[ind_message, msg, ind_entities,
                                       freq, 'white']]
                    ind_message += 1
                if len(cluster[2][i][node_messages_examples:]) > 0:
                    relation_list += [
                        [ind_message, 'Outras frases', ind_entities,
                         freq_others, 'white']]
                    ind_message += 1
            ind_entities += 1
    return relation_list


def sorted_cluster(parent_entity_dict: dict,
                   filtered_messages_dict: dict) -> list:
    """Sort cluster by frequency

    Parameters
    ----------
    parent_entity_dict: dict
        dictionary with the relation entity-cluster.
    filtered_messages_dict: dict
        dictionary with the relation entity-message

    Returns
    -------
    list
        a list with the clusters, entities and message sorted by frequency
    """
    output = []
    for key, value in parent_entity_dict.items():
        sorted_entity, freq, msg_list = sorted_entities(value,
                                                        filtered_messages_dict)
        aux_list = [key, sorted_entity, msg_list, freq]
        output.append(aux_list)
    return sorted(output, key=operator.itemgetter(3), reverse=True)


def sorted_entities(entities_list: list,
                    filtered_messages_dict: dict) -> tuple:
    """Sort entities by frequency


    Parameters
    ----------
    entities_list: list
        list with the entities of a cluster.
    filtered_messages_dict: list
        dictionary with the relation entity-message

    Returns
    -------
    tuple
        the sorted entities, the cumulative frequency and sorted messages.
    """
    aux_list = []
    for entity in entities_list:
        sorted_messages = sorted(filtered_messages_dict[entity],
                                 key=operator.itemgetter(1), reverse=True)

        aux_list.append([entity, sorted_messages,
                         sum(value[1] for value in sorted_messages)])
    aux_list = sorted(aux_list, key=operator.itemgetter(2), reverse=True)
    entities_sorted = [value[0] for value in aux_list]
    msg_sorted = [value[1] for value in aux_list]
    freq = sum([value[2] for value in aux_list])
    return entities_sorted, freq, msg_sorted


def create_entity_hierarchy(filtered_messages_frequency_dict: dict,
                            parent_entity_dict: dict,
                            node_messages_examples: int) -> str:
    """Create the html with the tree representation

    Parameters
    ----------
    filtered_messages_frequency_dict: dict
        dictionary with the relation entity-message
    parent_entity_dict: dict
        dictionary with the relation entity-cluster.
    node_messages_examples: int
        maximum of leaves in a branch.

    Returns
    -------
    str
        a string for the html
    """
    relation_list = [[0, 'Assuntos', -1, 1, 'white']]
    relation_list = add_entities(relation_list, parent_entity_dict,
                                 filtered_messages_frequency_dict,
                                 node_messages_examples)
    html = """<html>
      <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
          google.charts.load('current', {packages:['wordtree']});
          google.charts.setOnLoadCallback(drawSimpleNodeChart);
          function drawSimpleNodeChart() {
            var nodeListData = new google.visualization.arrayToDataTable([
              ['id', 'childLabel', 'parent', 'size', { role: 'style' }],
              %s);

            var options = {
              backgroundColor: '#262730',
              fontName: 'Times-Roman',
              wordtree: {
                format: 'explicit',
                type: 'suffix'
              }           
            };

            var wordtree = new google.visualization.WordTree(document.getElementById('wordtree_explicit'));
            wordtree.draw(nodeListData, options);
          }
        </script>
      </head>
      <body>
        <div id="wordtree_explicit" style="width: 1500px; height: 1200px;"></div>
      </body>
    </html>""" % (str(relation_list)[1:])
    return html


def create_hierarchy_frequency_dict(entity_frequency_dict: dict,
                                    parent_entity_dict: dict) -> tp.Tuple[
    dict, dict]:
    """
    Create a dictionary as the example:

    {groups: [{name: cartão, frequency: 400, children: [{name: cartão de
    crédito, frequency: 129}, {name: cartão de débito, frequency: 81},
    name: cartão, frequency: 200}]}]}

    Parameters
    ----------
    entity_frequency_dict: dict
        dictionary with the relation entity-frequency
    parent_entity_dict: dict
        dictionary with the relation parent-entities

    Returns
    -------
    tp.Tuple[dict, dict]
        tuple with dictionary with information about the clusters and a
        dictionary with the frequency of each cluster.
    """
    parent_dict = {}
    output_list = []
    for key, value in parent_entity_dict.items():
        children_list = []
        frequency = 0
        for entity in value:
            children_list.append({'name': entity,
                                  'frequency': entity_frequency_dict[entity]})
            frequency += entity_frequency_dict[entity]

        parent_dict[key] = frequency
        hierarcy_frequency_dict = {'name': key,
                                   'frequency': frequency,
                                   'children': children_list}
        output_list.append(hierarcy_frequency_dict)
    return {'group': output_list}, parent_dict


def save_entity_hierarchy(full_path: str, entity_hierarchy_html: str) -> None:
    """
    Parameters
    ---------
    full_path : str
        String with the path to save the file
    entity_hierarchy_html : str
        HTML with the entities relation.
    """
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(entity_hierarchy_html)


def save_entity_hierarchy_dict(full_path: str,
                               entity_hierarchy_dict: dict) -> None:
    """
    Parameters
    ---------
    full_path : str
        String with the path to save the file
    entity_hierarchy_dict : dict
        dictionary with information about the clusters
    """
    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(entity_hierarchy_dict, f, ensure_ascii=False)


def save_top_plot(full_path: str, topic_freq_dict: dict) -> None:
    """
    Parameters
    ---------
    full_path : str
        String with the path to save the file
    topic_freq_dict : dict
        dictionary with the frequency of each topic.
    """
    sorted_dict = {k: v for k, v in sorted(topic_freq_dict.items(),
                                           key=lambda item: item[1],
                                           reverse=True)}
    subjects = [sub.capitalize() for sub in list(sorted_dict.keys())[:5]]
    values = list(sorted_dict.values())[:5]

    subjects.reverse()
    values.reverse()

    fig = px.bar(y=subjects,
                 x=values,
                 color_discrete_sequence=px.colors.qualitative.G10,
                 title="Analisando top 5 assuntos",
                 template='simple_white',
                 orientation='h',
                 labels={'x': 'Frequência',
                         'y': 'Assuntos'})
    fig.update_layout(autosize=False,
                      width=500,
                      height=500)
    fig.update_traces(width=0.8)
    fig.write_image(full_path)
