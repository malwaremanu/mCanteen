import React from 'react';
import {
  Page,
  Navbar,
  NavbarBackLink,
  Badge,
  Block,
  BlockTitle,
  List,
  ListGroup,
  ListItem,
} from 'konsta/react';

export default function ListPage() {
  return (
    <Page>
      <Navbar
        title="List"
        />

      <BlockTitle>Simple List</BlockTitle>
      <List>
        <ListItem title="Item 1" />
        <ListItem title="Item 2" />
        <ListItem title="Item 3" />
      </List>

      <BlockTitle>Simple Links List</BlockTitle>
      <List>
        <ListItem title="Link 1" link />
        <ListItem title="Link 2" link />
        <ListItem title="Link 3" link />
      </List>
    </Page>
  );
}